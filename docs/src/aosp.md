# AOSP

## Download source

```
# Ref: https://mirrors.tuna.tsinghua.edu.cn/help/git-repo/
curl https://mirrors.tuna.tsinghua.edu.cn/git/git-repo -o repo
chmod a+x repo
export REPO_URL='https://mirrors.tuna.tsinghua.edu.cn/git/git-repo/'

mkdir WORKING_DIRECTORY
cd WORKING_DIRECTORY
repo init -u https://aosp.tuna.tsinghua.edu.cn/platform/manifest
repo init -u https://aosp.tuna.tsinghua.edu.cn/platform/manifest -b android-11.0.0_r8
repo sync
```

## Creating a case-sensitive disk image for OSX

```
hdiutil create -type SPARSE -fs 'Case-sensitive Journaled HFS+' -size 160g android.dmg

# If you need a larger volume later, you can resize the sparse image with the following command
hdiutil resize -size <new-size-you-want>g android.dmg.sparseimage

# Mount the android file image
hdiutil attach android.dmg.sparseimage -mountpoint mountpoint

# Unmount the android file image
hdiutil detach mountpoint
```

## How to just build Android system image

Remember to run `source build/envsetup.sh && lunch` to choose a target when in a new terminal.

If your changes effect other applications, use make systemimage, otherwise use make snod.

Notice: `make systemimage` will check dependency during compile progress, while `make snod` will not do this check, so the former command need more time than the latter.

## How to manage ramdisk.img

```
# Extract (It's highly possible that ramdisk.img actually is a gzip file)
cd a-clean-folder # e.g. a sub folder
gunzip -c ../ramdisk.img | cpio -idm

# Create
cd path-to-ramdisk
find . | cpio -o -Hnewc | gzip -9 > ../ramdisk.img
```

## Run emulator

```
./prebuilts/android-emulator/linux-x86_64/emulator -kernel prebuilts/qemu-kernel/arm64/kernel-qemu -ramdisk out/target/product/generic/ramdisk.img -system out/target/product/generic/system.img -memory 2048  -no-window -verbose

# With userdata.img
./prebuilts/android-emulator/linux-x86_64/emulator -kernel prebuilts/qemu-kernel/arm64/kernel-qemu -ramdisk out/target/product/generic/ramdisk.img -system out/target/product/generic/system.img -sysdir out/target/product/generic -data out/target/product/generic/userdata.img -scale 0.7 -memory 2048  -partition-size 4096 -no-window -verbose

# May need to export ANDROID_BUILD_TOP and ANDROID_PRODUCT_OUT.
# ANDROID_BUILD_TOP should point to root directory of the source tree.
# ANDROID_PRODUCT_OUT should point to the directory that contains generated images.
export ANDROID_BUILD_TOP=~/aosp
export ANDROID_PRODUCT_OUT=~/aosp/out/target/product/generic_x86_64

# Run for x86_64 arch
./prebuilts/android-emulator/linux-x86_64/emulator -kernel prebuilts/qemu-kernel/x86_64/kernel-qemu -ramdisk out/target/product/generic_x86_64/ramdisk.img -system out/target/product/generic_x86_64/system.img -sysdir out/target/product/generic_x86_64 -data out/target/product/generic_x86_64/userdata.img -scale 0.7 -memory 2048  -partition-size 4096 -no-window -verbose

# With kernel-ranchu, and without CPU accelerator
./prebuilts/android-emulator/linux-x86_64/emulator -kernel out/target/product/generic_x86_64/kernel-ranchu -ramdisk out/target/product/generic_x86_64/ramdisk.img -system out/target/product/generic_x86_64/system.img -sysdir out/target/product/generic_x86_64 -data out/target/product/generic_x86_64/userdata.img -memory 2048 -no-window -verbose -no-accel

# With customized qemu emulator, customized kernel, show kernel message, 1 CPU core, and redirect output to debug.log file
./android-qemu/objs/emulator -kernel ~/android-kernel/goldfish/arch/x86_64/boot/bzImage -ramdisk ~/aosp/out/target/product/generic_x86_64/ramdisk.img -system ~/aosp/out/target/product/generic_x86_64/system.img -sysdir ~/aosp/out/target/product/generic_x86_64 -data ~/aosp/out/target/product/generic_x86_64/userdata.img -memory 2048 -no-window -verbose -no-accel -show-kernel -ranchu -cores 1 >debug.log

# We can also feed emulator with `-debug all`, that will enable emulator debug log.
```

## Update working tree

```
# Fetch updates from remote
repo sync

# Only update working tree, don't fetch
repo sync -l
```

## Download and build kernel source

```
git clone https://aosp.tuna.tsinghua.edu.cn/kernel/goldfish
cd goldfish
git checkout -b android-4.14 remotes/origin/android-4.14
make x86_64_ranchu_defconfig
make -j4
```

## Download and build emulator

```
mkdir emu-master-dev
cd emu-master-dev
repo init -u https://aosp.tuna.tsinghua.edu.cn/platform/manifest -b emu-master-dev
repo sync

cd android
source envsetup.sh

# This will rebuild all, and cache will not be used. (We must execute this for initial setup)
./rebuild.sh

# After initial setup, and ./objs/build.ninja exists, we can do this
cd objs && ninja
```

## Trouble shooting

### When running emulator on OSX, it throws: 'dyld: Library not loaded: @rpath/libQt5CoreAndroidEmu.5.12.1.dylib'

```
# Suppose current working directory is the qemu root directory.
export DYLD_LIBRARY_PATH=$(pwd)/android/objs/lib64/qt/lib:$(pwd)/android/objs/lib64
```

## Too many open files

You need to increase open file descriptors limit by `ulimit -S -n 2048`. The change is only for current shell.
You may want to add it to shell startup file to make the change permanently.

On OSX, we can also use `launchctl limit` to change the limit. Using `launchctl limit` will make the change permanently.
If you're using iTerm, be sure to restart it after you make that change.

```
# Display all kinds of limits
sudo launchctl limit

# Set soft limit to 2048, and hard limit to unlimited
sudo launchctl limit maxfiles 2048 unlimited

# Set both soft and hard limit to 2048
sudo launchctl limit maxfiles 2048
```

## Emulator

```
# Add custom kernel command parameter
# Ref: https://www.kernel.org/doc/html/v4.14/admin-guide/kernel-parameters.html
# https://developer.android.com/studio/run/emulator-commandline
emulator -show-kernel @myavd1 -qemu -append printk.devkmsg=on >tmp1.log

emulator @myavd1 -shell -shell-serial tcp::4444,server,nowait
telnet localhost 4444

# Show qemu options
emulator -verbose

# Root access
adb root
adb shell
```

### Cross compile emulator for Windows on Linux

First, you need to have a Windows system to export the Windows SDK.

`package_from_installed.py` exists under
`$AOSP_DIR/external/qemu/android/third_party/chromium/depot_tools/win_toolchain`.
It can also be found at
`https://chromium.googlesource.com/chromium/tools/depot_tools/+/master/win_toolchain/`.

```
# Go to C:\Program Files (x86)\Windows Kits\10\Include to find a desired windows
# SDK version.
#
# And specify the visual studio version which is installed on your system (the
# script supports VS 2015 and 2017).
python.exe package_from_installed.py -w YOUR_WINDOWS_SDK_VERSION 2015|2017
```

A {hash}.zip file will be generated under your current working directory. Move
that file to the build machine.

### WIP

```
export DEPOT_TOOLS_WIN_TOOLCHAIN_BASE_URL=~/win_toolchain

./rebuild.sh --target=windows --no-tests
```

OR

```
$AOSP_DIR/prebuilts/android-emulator-build/common/ciopfs/linux-x86_64/ciopfs -o use_ino $DATA_POINT $MOUNT_POINT

# The backing file system should be case-insensitive.
export OPT_VSDIR=

./rebuild.sh --target=windows --no-tests
```

## Repo

* list available branches

https://stackoverflow.com/questions/2874347/how-to-display-available-branches-in-android-source-tree
https://android.googlesource.com/platform/manifest

https://source.android.com/setup/develop/repo

* Only single branch is fetched, if you want to change to another branch, you
  must redo a `repo init` with specific branch

## Kernel

https://source.android.com/setup/build/building-kernels

### What happens if I unlock bootloader?

Android mobile manufacturers are very serious about security so they have
purposefully shipped devices with a locked bootloader. But users have the option
to manually unlock it. Once you unlock your device’s bootloader, you can do all
types of customization like installing Custom ROMs, recovery and MODs but you
will lose the warranty too.

### How to unlock the bootloader of an Android phone?

Unlocking bootloader will wipe all of your data in the phone, and the phone will
be reset into factory mode.

```
# Connect the phone to PC via USB and reboot it into bootloader mode.
adb reboot bootloader

# After entering into bootloader mode, unlock the bootloader.
# It may ask for your confirmation, you may need to use volume button to select
# yes or no.
#
# `fastboot` executable is in the same bundle `platform-tools` as `adb`.
fastboot oem unlock

# What does this do?
fastboot flashing unlock

# After unlocking, reboot the phone. The phone may restart several times, and
# finally guide you to reinitialize the phone.
fastboot reboot

fastboot unlock-info?
```

## How to install TWRP recovery.img?

```
fastboot flash recovery recovery.img
fastboot boot recovery.img
```

There are three boot modes:

* Recovery mode
* Fastboot (bootloader) mode
* Normal mode
