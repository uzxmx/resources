# ImageMagick

## Resize

```
convert input.png -resize 300 output.png
convert input.png -resize 300x300 output.png
```

## How to create a canvas?

```
convert -size 300x300 canvas:white output.png
```

Ref: https://www.imagemagick.org/Usage/canvas/

## Replace white color with transparency

```
convert input.png -transparent white output.png

# If not perfectly white, use `-fuzz`
convert input.png -fuzz 30% -transparent white output.png
```

## Replace transparency with white color

```
convert input.png -background white -alpha remove -alpha off output.png
```

## Crop (cut borders)

```
input.jpg size: 860x860
target size: 750x750

# +55+55: left,top
# -55-55: right,bottom
size=55
convert input.jpg -crop +${size}+${size} -crop -${size}-${size} output.png
```

Ref:

* https://stackoverflow.com/questions/50494810/chop-4-sides-of-image-with-imagemagick
* https://superuser.com/questions/1161340/how-to-crop-an-image-using-imagemagick-from-the-command-line/1161341

## Remove borders

```
convert input.jpg -trim output.jpg
convert input.jpg -fuzz 5% -trim output.jpg
```

## Add borders

```
# The extent option specifies the final size.
convert input.png -background none -gravity center -extent 400x400 output.png

# Another method is to specify the delta size.
convert input.png -bordercolor none -border 20 output.png
convert input.png -bordercolor white -border 20 output.png
```

## Flip

```
# Flip up and down.
convert -flip foo.png bar.png

# Flip left and right.
convert -flop foo.png bar.png
```

## Get density of an image

```
# If the `units` is `Undefined`, it means `PixelsPerInch`.
identify -format "Density: %x x %y \nUnits: %U \nSize: %w x %h" input.svg
```

## Convert SVG to PNG

```
# The generated image doesn't look good on Mac OSX.
convert -background none -resize 500 input.svg output.png

in_density="$(identify -format "%x" input.svg)"
out_width=500

magick input.svg -density "%[fx:(($out_width/w)*$in_density)]" -delete 0 -background none input.svg -scale ${out_width}x output1.png

# The generated image looks good, but the width may be less than `${out_width}`.
magick input.svg -density "%[fx:(($out_width/w)*72)]" -delete 0 -background none input.svg output2.png

# The generated image looks good, and the width is equal to `${out_width}`.
magick input.svg -density "%[fx:(($out_width/w)*96)]" -delete 0 -background none input.svg output3.png
```

Ref: https://stackoverflow.com/questions/9853325/how-to-convert-a-svg-to-a-png-with-imagemagick
