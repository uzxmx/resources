# gclient

## fetch v.s. gclient

TODO

`fetch` command will generate a `.gclient` file, and then runs `gclient sync`.

## gclient sync

If you copy the whole chromium source directory from Linux to Mac OSX, then
running `gclient sync` will download required dependencies fro Mac OSX, and
`.gclien_entries` is updated automatically.

## gclient mirror

We can update the url in `.gclient` to a mirror url. Then run `gclient sync`.
This works for v8. (https://codechina.csdn.net/mirrors/v8/v8.git) But
dependencies may fail to download.

## Troubleshooting

If `.cipd_bin` is too old, it may cause some error. We can delete that
directory so that it can be generated automatically.
