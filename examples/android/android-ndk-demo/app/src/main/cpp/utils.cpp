#include <jni.h>
#include <string>

#include "log.hpp"

static void JNICALL nativeFoo(JNIEnv* env, jobject obj) {
    log_info("JNIUtils", "nativeFoo");
}

static jboolean JNICALL staticNativeBar(JNIEnv* env, jclass clazz, jstring arg1, jint arg2) {
    const char* str = env->GetStringUTFChars(arg1, 0);
    log_info("JNIUtils", "staticNativeBar: %s, %d", str, arg2);
    env->ReleaseStringUTFChars(arg1, str);
    return false;
}

extern "C" JNIEXPORT jstring JNICALL
Java_com_example_android_MainActivity_stringFromJNI(
        JNIEnv* env,
        jobject /* this */) {
    std::string hello = "Hello from C++";
    return env->NewStringUTF(hello.c_str());
}

extern "C" JNIEXPORT jint JNICALL
Java_com_example_android_MainActivity_sum(
        JNIEnv* env,
        jobject obj,
        jint a,
        jint b) {
    log_info("MainActivity", "a: %d, b: %d", a, b);
    return a + b;
}

/**
 * There are two ways to register native methods. One way is to define the function by using a
 * proper name. The other way is to call `RegisterNatives` in `JNI_OnLoad`.
 */
JNIEXPORT jint JNI_OnLoad(JavaVM* vm, void* reserved) {
    JNIEnv* env;
    if (vm->GetEnv(reinterpret_cast<void**>(&env), JNI_VERSION_1_6) != JNI_OK) {
        return JNI_ERR;
    }

    // Find your class. JNI_OnLoad is called from the correct class loader context for this to work.
    jclass c = env->FindClass("com/example/android/JNIUtils");
    if (c == nullptr) return JNI_ERR;

    // Register your class' native methods.
    static const JNINativeMethod methods[] = {
        {"nativeFoo", "()V", reinterpret_cast<void*>(nativeFoo)},
        {"staticNativeBar", "(Ljava/lang/String;I)Z", reinterpret_cast<void*>(staticNativeBar)},
    };
    int rc = env->RegisterNatives(c, methods, sizeof(methods)/sizeof(JNINativeMethod));
    if (rc != JNI_OK) return rc;

    return JNI_VERSION_1_6;
}
