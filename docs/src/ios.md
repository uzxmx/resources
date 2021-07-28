# iOS

## Debug iOS WKWebview based application or mobile website by desktop Safari

The WKWebview based application should be built in debug configuration. Or the
mobile website should be opened in iOS Safari.

In desktop Safari, enable develop menu. Connect iOS device to the desktop (via
USB cable), then the device should appear in the develop menu.

If it shows `No web inspector`, then on iOS device, go to Settings -> Safari ->
Advanced -> Enable web inspector.

## Use a local server by IP address for development

When `NSAppTransportSecurity` is enabled, you may specify `NSExceptionDomains`
to include the servers you want to access. Those servers would better to have a
domain name, because for some iOS versions, servers specified by an IP address
are not supported. To work around this, you can disable `NSAppTransportSecurity`
temporarily as shown below.

```
<key>NSAppTransportSecurity</key>
<dict>
  <key>NSAllowsArbitraryLoads</key>
  <true/>
</dict>
```

Ref: https://stackoverflow.com/questions/30903923/app-transport-security-and-ip-addresses-in-ios9
