# Android

## Build android app with Android Studio builtin java

For Mac OSX,

```
export JAVA_HOME="/Applications/Android Studio.app/Contents/jre/jdk/Contents/Home"
```

For more information, please search ANDROID_STUDIO_HOME in `~/.dotfiles/zshrc.local.erb`.

## 为Arduino供电

https://blog.csdn.net/chenchen2360060/article/details/95120577

## fastboot

Recovery mode
Fastboot mode
Normal boot

```
# Enter into fastboot mode
adb reboot bootloader

# Enter into recovery mode
adb reboot recovery

# Enter into normal boot
fastboot reboot

fastboot devices
# You may need to enable oem unlock in android settings.
# Unlocking bootloader may remove user data.
fastboot oem unlock
```

Refs:

金立F100S官方刷机包：http://url88.cn/u/JoEFu?keyword=F100
Root: https://gearallnews.com/how-to-root-gionee-f100-and-install-twrp-recovery/
Root: https://rootmygalaxy.net/how-to-root-gionee-f100-and-install-twrp-recovery/
Create device tree from rom: https://forum.xda-developers.com/android/software-hacking/how-to-create-device-tree-android-rom-t3498355

## https://dontkillmyapp.com/
