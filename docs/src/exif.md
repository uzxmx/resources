# Exif

Exif means exchangeable image file format.

## Orientation

### Show orientation

```
# Output human-readable value.
# Empty output may mean normal (non-rotated).
exiftool -Orientation foo.jpg

# Output machine-readable value.
exiftool -Orientation -n foo.jpg
```

### Modify orientation

```
# Change to non-rotated orientation.
exiftool -Orientation=1 -n image.jpg

# Change to `Rotate 90 CW`.
exiftool -Orientation=6 -n image.jpg
```

Ref: https://superuser.com/questions/435443/how-can-i-modify-the-exif-orientation-tag-of-an-image

### Some orientation values

```
1: rotate(0deg)
3: rotate(180deg)
6: rotate(90deg)
8: rotate(270deg)
```
