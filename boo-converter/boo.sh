#!/bin/bash

# take a GIF and turn it into a BMP animation for the boo
#
name=`basename $1 .gif`
echo Converting $name.gif to $name.bmp animation for boo

# split the gif into temporary PNGs
#
convert $name.gif $name-%d.png

# rezie and mono them
#
mogrify -resize 64x128 -monochrome -negate -rotate 90 $name-*.png 

# glue them together
#
convert +append '$name-*.png' $name.bmp

# delete temp files
#
#rm $name-*.png
