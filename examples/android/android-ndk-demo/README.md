# android-ndk-demo

```
debug jnish

adb forward --remove tcp:22527
adb forward tcp:22527 tcp:53289
nc localhost 22527

getStringUTFChars 549013556632
getStringUTFChars 0x7fd3c20d98
getObjectClass 549013556628
```

### How to run

```
# Build apk.
android build

# Only build for `armeabi-v7a` abi.
android build - -Pabi=armeabi-v7a

# Disable arm neon support. When neon is enabled, lldb may fail to disassemble
# machine instructions, and show unknown opcode.
#
# Instead of using below option, we can also specify `disableArmNeon=1` in
# `local.properties`.
android build - -Pabi=armeabi-v7a -PdisableArmNeon=1
```


abi=armeabi-v7a
disableArmNeon=1

```
        externalNativeBuild {
            cmake {
                // See https://developer.android.com/ndk/guides/cmake#android_arm_neon
                if (project.hasProperty('disableArmNeon') && project.disableArmNeon.toString().equals("1")) {
                    print("---------")
                    print(project.disableArmNeon)
                    print(project.disableArmNeon.equals("1"))
                    arguments '-DANDROID_ARM_NEON=FALSE'
                } else {
                    arguments '-DANDROID_ARM_NEON=TRUE'
                }
                cppFlags ''
            }
        }

        ndk {
            if (project.hasProperty('abi')) {
                abiFilters.addAll(project.abi.split(','))
            } else {
                abiFilters 'armeabi-v7a', 'arm64-v8a', 'x86', 'x86_64'
            }
        }
```
