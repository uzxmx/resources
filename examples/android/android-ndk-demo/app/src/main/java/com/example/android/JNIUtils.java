package com.example.android;

public class JNIUtils {

    public native void nativeFoo();

    public static native boolean staticNativeBar(String arg1, int arg2);
}
