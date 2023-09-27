#include <string.h>
#include <stdio.h>
#include <iostream>
#include <jni.h>
#include <pthread.h>
#include <sys/socket.h>
#include <netinet/in.h>

#include "log.hpp"

const char* TAG = "JNISH";

JavaVM* globalVM;
JNIEnv* env;
pthread_t thread;

class Args {
public:
    Args(const char* args, int size);
    ~Args();

    int GetLen();
    const char* GetAt(int i);
    long long GetIntAt(int i);

private:
    char *_copy;
    int _len;
    char **_args;
};

Args::Args(const char *args, int size) {
    _copy = new char[size + 1];
    _copy[size] = '\0';
    strncpy(_copy, args, size);

    _args = new char*[100];
    int i = 0;
    char* arg = NULL;
    int arg_idx = 0;
    while (i < size) {
        if (_copy[i] == ' ') {
            if (arg) {
                _args[arg_idx++] = arg;
                arg = NULL;
                _copy[i] = NULL;
            }
        } else if (!arg) {
            arg = _copy + i;
        }
        i++;
    }
    if (arg) {
        _args[arg_idx++] = arg;
    }
    _len = arg_idx;
}

Args::~Args() {
    if (_args) {
        delete _args;
    }
    if (_copy) {
        delete _copy;
    }
}

int Args::GetLen() {
    return _len;
}

const char * Args::GetAt(int i) {
    return _args[i];
}

long long Args::GetIntAt(int i) {
    auto arg = _args[i];
    log_info(TAG, "arg %d: %s", i, arg);
    if (arg[0] == '0' && (arg[1] == 'x' || arg[1] == 'X')) {
        // TODO long long or unsigned long long?
        return std::stoull(arg, nullptr, 16);
    } else {
        return atoll(arg);
    }
}

void handle_command(int fd, const char* command, const char* args, int args_size) {
    int size = 10240;
    char* resp = new char[size];
    memset(resp, 0, size);
    if (!strcmp(command, "getVersion")) {
        sprintf(resp, "Version: %d\n", env->GetVersion());
    } else if (!strcmp(command, "getStringUTFChars")) {
        auto arguments = Args(args, args_size);
        if (arguments.GetLen() < 1) {
            sprintf(resp, "Wrong arguments\n");
            goto end;
        }
        jstring pointer = (jstring) arguments.GetIntAt(0);
        const char* str = env->GetStringUTFChars(pointer, 0);
        sprintf(resp, "StringUTFChars(%llx): %s\n", pointer, str);
        env->ReleaseStringUTFChars(pointer, str);
    } else if (!strcmp(command, "getObjectClass")) {
        auto arguments = Args(args, args_size);
        if (arguments.GetLen() < 1) {
            sprintf(resp, "Wrong arguments\n");
            goto end;
        }
        jobject pointer = (jobject) arguments.GetIntAt(0);

        jclass cls = env->GetObjectClass(pointer);
//        jclass globalClass = reinterpret_cast<jclass>(newEnv->NewGlobalRef(cls));
        log_info(TAG, "After GetObjectClass: %llx, %llx, %llx",cls, pointer, env);
        jmethodID mid = env->GetMethodID(cls, "getClass", "()Ljava/lang/Class;");
        log_info(TAG, "After 1");
//        jobject cls_obj = env->CallObjectMethod(pointer, mid);
//        log_info(TAG, "After 2");
//
//        cls = env->GetObjectClass(cls_obj);
//        mid = env->GetMethodID(cls, "getName", "()Ljava/lang/String;");
//        log_info(TAG, "After GetMethodId");
//
//        jstring cls_name = (jstring) env->CallObjectMethod(cls_obj, mid);
//        log_info(TAG, "After CallObjectMethod");
//
//        const char* str = env->GetStringUTFChars(cls_name, 0);
//        log_info(TAG, "str: %s", str);
//        sprintf(resp, "getObjectClass(%llx): %s\n", pointer, str);
//        env->ReleaseStringUTFChars(cls_name, str);

//        env->DeleteLocalRef(cls_obj);
    }

end:
    int len = strlen(resp);
    if (len > 0) {
        send(fd, resp, len, 0);
    }

    delete resp;
}

void run(void *args) {
    auto status = globalVM->AttachCurrentThreadAsDaemon(&env, NULL);
    if (status != JNI_OK) {
        log_error(TAG, "Failed to attach");
    }

    log_info(TAG, "Thread started");

    struct sockaddr_in server_addr;
    memset(&server_addr, 0, sizeof(server_addr));
    server_addr.sin_family = AF_INET;
    server_addr.sin_addr.s_addr = INADDR_ANY;
//    server_addr.sin_port = htons(22528);
    server_addr.sin_port = 0;

    int server_socket_fd = socket(PF_INET, SOCK_STREAM,0);
    if (server_socket_fd < 0) {
        log_error(TAG, "Failed to create server socket");
        return;
    }

    bind(server_socket_fd, (struct sockaddr*)&server_addr, sizeof(server_addr));
    socklen_t len;
    getsockname(server_socket_fd, (struct sockaddr*)&server_addr, &len);
    log_info(TAG, "Listening at port %d", ntohs(server_addr.sin_port));

    listen(server_socket_fd,6);

    struct sockaddr_in client_addr;
    socklen_t sin_size = sizeof(struct sockaddr_in);
    while (true) {
        int client_socket_fd = accept(server_socket_fd, (struct sockaddr*)&client_socket_fd, &sin_size);
        if (client_socket_fd < 0){
            log_error(TAG, "Failed to accept");
            return;
        }

        int buf_size = 10240;
        char buf[buf_size];
        int len = 0;
        while (true) {
            log_info(TAG, "Start to read");
            len = recv(client_socket_fd, buf, buf_size, 0);
            if (len < 0) {
                log_error(TAG, "Some error happened");
                break;
            }
            if (len == 0) {
                log_info(TAG, "Client closed the connection");
                break;
            }
            log_info(TAG, "Read %d bytes", len);
            int i = 0;
            char* args = strchr(buf, ' ');
            if (!args) {
                log_info(TAG, "Cannot find a space");
                continue;
            }
            int n = args - buf;
            char* dest = new char[n + 1];
            dest[n] = '\0';
            strncpy(dest, buf, n);
            handle_command(client_socket_fd, dest, args, len - n);
            delete dest;
        }
    }
}

JNIEXPORT jint JNI_OnLoad(JavaVM* vm, void* reserved) {
//    if (vm->GetEnv(reinterpret_cast<void**>(&env), JNI_VERSION_1_6) != JNI_OK) {
//        return JNI_ERR;
//    }

    globalVM = vm;

    log_info(TAG, "Create thread");
    pthread_create(&thread, NULL, reinterpret_cast<void *(*)(void *)>(run), NULL);

    return JNI_VERSION_1_6;
}
