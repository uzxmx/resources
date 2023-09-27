#include <jni.h>
#include <string>
#include <math.h>

#include "log.hpp"

const char* TAG = "JNIUtils";

static void __attribute__ ((constructor)) init1(void) {
    double a = sqrt(4);
    log_info("JNIUtils", "init: %f", a);
}

static void __attribute__ ((constructor)) init2(void) {
    double a = sqrt(4);
    log_info("JNIUtils", "init2: %f", a);
}

static void __attribute__ ((constructor)) init3(void) {
    double a = sqrt(4);
    log_info("JNIUtils", "init3: %f", a);
}

static void JNICALL nativeFoo(JNIEnv* env, jobject obj) {
    log_info("JNIUtils", "nativeFoo");
}

static jboolean JNICALL staticNativeBar(JNIEnv* env, jclass clazz, jstring arg1, jint arg2) {
    const char* str = env->GetStringUTFChars(arg1, 0);
    log_info("JNIUtils", "staticNativeBar: %s, %d", str, arg2);
    env->ReleaseStringUTFChars(arg1, str);
    return false;
}

void funcWithJStringInner(JNIEnv* env, jobject obj, jstring arg) {
    const char* str = env->GetStringUTFChars(arg, 0);
    log_info(TAG, "funcWithJStringInner: %s", str);
    env->ReleaseStringUTFChars(arg, str);

    jclass cls = env->GetObjectClass(obj);
    log_info(TAG, "After GetObjectClass: %llx, %llx, %llx", cls, obj, env);
    jmethodID mid = env->GetMethodID(cls, "getClass", "()Ljava/lang/Class;");
    log_info(TAG, "After 1");
    jobject cls_obj = env->CallObjectMethod(obj, mid);
    log_info(TAG, "After 2");

    cls = env->GetObjectClass(cls_obj);
    mid = env->GetMethodID(cls, "getName", "()Ljava/lang/String;");
    log_info(TAG, "After GetMethodId");

    jstring cls_name = (jstring) env->CallObjectMethod(cls_obj, mid);
    log_info(TAG, "After CallObjectMethod");

    const char* s = env->GetStringUTFChars(cls_name, 0);
    log_info(TAG, "str: %s", s);
    env->ReleaseStringUTFChars(cls_name, s);
}

void JNICALL funcWithJString(JNIEnv* env, jobject obj, jstring arg) {
    log_info("JNIUtils", "funcWithJString: %llx %llx %llx", env, obj, arg);
    funcWithJStringInner(env, obj, arg);
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
        {"funcWithJString", "(Ljava/lang/String;)V", reinterpret_cast<void*>(funcWithJString)},
    };
    int rc = env->RegisterNatives(c, methods, sizeof(methods)/sizeof(JNINativeMethod));
    if (rc != JNI_OK) return rc;

    return JNI_VERSION_1_6;
}
