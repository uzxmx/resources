# Mac

## How to input number with circle around?

Switch to Chinese input method, and press `Shift + Option + b`.

## Run qemu with customized kernel

qemu-system-x86_64 -kernel ~/shared/bzImage -initrd ~/shared/initramfs.cpio.gz -nographic -append "console=ttyS0"

## Sync a single project from aosp

./repo sync $PROJECT_NAME --no-tags --no-clone-bundle

## Run objective-c test in console

```
xcodebuild -scheme Development -workspace Foo.xcworkspace/ -sdk iphonesimulator \
  -destination 'platform=iOS Simulator,name=iPhone 8,OS=12.1' \
  -only-testing:FooTests/BarSpec test | xcpretty --test --color

xcodebuild -scheme Development -workspace Foo.xcworkspace/ -sdk iphonesimulator \
  -destination 'platform=iOS Simulator,name=iPhone 8,OS=12.1' \
  -only-testing:FooTests/BarSpec test | xcpretty -tc
```

## xcodebuild actions

Use `man xcodebuild` to get all actions.

## Mount NTFS with RW permissions

```
# Find device through spotlight profile
sudo ntfs-3g /dev/disk2s3 /mount_point
```

Refs: https://github.com/osxfuse/osxfuse/wiki/NTFS-3G

## `date` gives wrong time (several seconds late)

For 10.14 Mojave, execute `sudo sntp -sS pool.ntp.org`.

Ref: https://apple.stackexchange.com/a/117865

## Use external monitor when lid is closed

```
sudo pmset -b disablesleep 1
# Or
sudo pmset -a disablesleep 1

# Restore
sudo pmset -b disablesleep 0
# Or
sudo pmset -a disablesleep 0
```

Ref:

* https://apple.stackexchange.com/a/356255
* https://www.reddit.com/r/MacOS/comments/a4jmqd/keeping_macbook_awake_while_closing_the_lid/


## Open xcode project from terminal

```
xed -b <directory>
```

## How to make clang show header search paths

```
clang -E -x c++ - -v < /dev/null
```

## Pod commands

```
# Show pod spec
pod spec cat Masonry
pod spec cat Masonry --verbose

# Show available versions of a pod
pod trunk info Masonry
```

### How to download a pod?

Use `pod spec cat` to find the source of the specified pod.

## How to use xcode beta version

By default xcode is installed at /Applications/Xcode.app/, after downloading a beta version,
you can put it into a different location in order not to affect the default version. In order
to activate it as the default developer directory, you can run:

```
xcode-select -s <path-to-your-new-xcode-version>/Contents/Developer
```

If you want to restore the active developer directory for the default xcode version, run:

```
xcode-select -s /Applications/Xcode.app/Contents/Developer
```

Run below if you want to show current active developer directory:

```
xcode-select -p
```

## Xcode build directory

The default build directory is `~/Library/Developer/Xcode/DerivedData`.

Ref: https://stackoverflow.com/a/5952841

## Use exception breakpoint

View -> Navigators -> Show Breakpoint Navigator

At the left-bottom of the panel, click `+` button, and select `Exception Breakpoint`.

## TODO why does an app built by two different versions of xcode behave differently in a same phone?

For example, an app built by xcode 10.2 works, but if built by xcode 11.2, it will throw
`Client error attempting to change layout margins of a private view`.

## How to make a bootable usb stick from an ISO file?

1. Convert .iso file to .img file:
   ```
   hdiutil convert -format UDRW -o /path/to/target.img /path/to/source.iso
   ```

   OS X tends to put the .dmg ending on the output file automatically. Rename the file by typing:

   ```
   mv /path/to/target.img.dmg /path/to/target.img
   ```

1. Run `diskutil list` to get the current list of devices

1. Insert your flash media

1. Run `diskutil list` again and determine the device node assigned to your flash media (e.g. /dev/disk2)

1. Run `diskutil unmountDisk /dev/diskN` (replace N with the disk number from the last command - in the previous example, N would be 2)

1. Execute `sudo dd if=/path/to/target.img of=/dev/rdiskN bs=1m`
   > Using /dev/rdisk instead of /dev/disk may be faster.

   > If you see the error dd: /dev/diskN: Resource busy, make sure the disk is not in use. Start the 'Disk Utility.app' and unmount (don't eject) the drive.

1. Run `diskutil eject /dev/diskN` and remove your flash media when the command completes

## Access iOS device and application from terminal (CLI)

```
# List all connected devices.
idevice_id

# List all USB-connected devices.
idevice_id -l

# List all network-connected devices.
# Devices may not be found automatically in the same network. You may need to
# first use an USB cable to connect, then remove the USB cable, it will be found
# via network.
idevice_id -n

# Get device name.
idevice_id <UDID>

# Show logs for a specific process from a network-connected iOS device.
idevicesyslog -n -p <process-id|name>

# Install iOS app through USB. (for network-connected device, it seems stuck at
# Uploading XXX.app package contents...)
# You may find an app built by xcode at ~/Library/Developer/Xcode/DerivedData/.
ideviceinstaller -i XXX.app
```

## Xcode troubleshooting

### error: module compiled with Swift 5.2.4 cannot be imported by the Swift 5.3 compiler: xxx.swiftmodule

#### How  to check the swift compiler version?

```
# Check the xcode version.
# xcode version matrix: https://developer.apple.com/support/xcode/
xcodebuild -version

# Check the swift compiler version.
swiftc -version
swift -version

# Check the swift compiler version in a non-active developer directory.
DEVELOPER_DIR=~/Downloads/Xcode-beta.app xcrun swiftc -version
```

#### How  to check the swift compiler version for an imported framework (*.swiftmodule)?

We may find the version in some header file. Search file with `[Ss]wift` as part
of the filename under the imported framework directory.


## IP forward
```
sysctl net.inet.ip.forwarding
sudo sysctl -w net.inet.ip.forwarding=1
```

## Extract .xip file

```
# Contents will be extracted into current working directory. So in order to
# extract to a specific location, we can change to a desired directory before
# executing `xip`.
xip --expand <path_to_xip_file>
```

## Find hostnames in a LAN

```
brew install arp-scan
arp-scan --localnet
```

```
# nc timeout
nc -zv -G 2 -w 2 "$line" 22
https://stackoverflow.com/questions/24198456/issue-with-netcat-timeout
```

## Show the UUID for each architecture of .dSYM files

```
# You can find .dSYM folder by xcode (View -> Navigators -> Reports), which is
# specified by the environment variable `DWARF_DSYM_FOLDER_PATH`.
dwarfdump -u <file>
```

## How to download IPA file from AppStore

Using Apple Configurator 2:

1. Download an app from App Store to you phone
1. Open Apple Configurator 2 on your Mac and log into your Apple account
1. Connect your phone to your Mac using a USB cable
1. Into Apple Configurator 2 select your phone
1. Then tap on the “Add” button in the top, then tap on “Apps” button
1. Choose the app and tap on “Add” button
1. Finally it could tell you an app already exists, but don’t worry — just be in a hurry to grab an .ipa using this path: `~/Library/Group\ Containers/K36BKF7T3D.group.com.apple.configurator/Library/Caches/Assets/TemporaryItems/MobileApps/`

Ref: https://medium.com/xcnotes/how-to-download-ipa-from-app-store-43e04b3d0332
