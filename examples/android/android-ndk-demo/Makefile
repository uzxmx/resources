build:
	android build - -Pabi=armeabi-v7a,arm64-v8a,x86,x86_64

build-armv7:
	android build - -Pabi=armeabi-v7a

build-arm64:
	android build - -Pabi=arm64-v8a

build-with-frida: build
	cp app/build/outputs/apk/debug/app-debug.apk frida/src.apk
	cd frida && PATH=~/Library/Android/sdk/build-tools/31.0.0:$$PATH android-inject-frida-gadget -s src.apk -a armeabi-v7a,arm64-v8a,x86,x86_64
	cd frida && adb install src.objection.apk
	adb shell am start -n com.example.android/com.example.android.MainActivity

install:
	adb install app/build/outputs/apk/debug/app-debug.apk

start:
	adb shell am start -n com.example.android/com.example.android.MainActivity

debug:
	cd lldb && android-debug com.example.android com.example.android.MainActivity
