Auto-generate Android icons for multiple densities

Frustrated with resizing icons for multiple screen orientations and densities?  This python script will automatically generate optimized icons for your Android app for all 'standard' densities! 

Simply run the script with the path to the image you want to convert into multiple densities:

android-iconify.py icon_file_to_convert.png

The script will generate the standard Android res/ directory structure (res/drawable-ldpi, etc) and rename and resize the image to the suggested Android developer practices (eg. /res/drawable-ldpi/ic_launcher_icon). Naming and sizing based on:

http://developer.android.com/guide/practices/ui_guidelines/icon_design.html

The script requires only python and imagemagick.  On Ubuntu compatible systems, this can be done using apt:

sudo apt-get install python2.6 imagemagick

