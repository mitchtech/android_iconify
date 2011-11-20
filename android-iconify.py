#!/usr/bin/python
"""
@file android_iconify.py
@author Michael Mitchell
@date Sept 18, 2011
@brief Automate the re-sizing of icons for Android using python and ImageMagick.
@usage android-iconify.py icon_file_to_convert.png

Naming and sizing based on suggested developer practices here:

http://developer.android.com/guide/practices/ui_guidelines/icon_design.html
"""
import os, sys

if len(sys.argv) != 2:  # the program name and image file.png
  sys.exit("Usage: android_iconify.py icon_file_to_convert.png")

file = sys.argv[1]
if file.endswith('.png'):
	# create directory structure
	newdir = ('./res')
	os.mkdir(newdir)
	newdir = ('./res/drawable-ldpi')
	os.mkdir(newdir)
	newdir = ('./res/drawable-mdpi')
	os.mkdir(newdir)
	newdir = ('./res/drawable-hdpi')
	os.mkdir(newdir)
	newdir = ('./res/drawable-xhdpi')
	os.mkdir(newdir)
	# drawable-ldpi
	new = ('./res/drawable-ldpi/ic_launcher_' + file)
	os.system ("convert %s -resize 36x36 %s" % (file, new))
	new = ('./res/drawable-ldpi/ic_stat_notify_' + file)
	os.system ("convert %s -resize 18x18 %s" % (file, new))
	# drawable-mdpi
	new = ('./res/drawable-mdpi/ic_launcher_' + file)
	os.system ("convert %s -resize 48x48 %s" % (file, new))
	new = ('./res/drawable-mdpi/ic_stat_notify_' + file)
	os.system ("convert %s -resize 24x24 %s" % (file, new))
	# drawable-hdpi
	new = ('./res/drawable-hdpi/ic_launcher_' + file)
	os.system ("convert %s -resize 72x72 %s" % (file, new))
	new = ('./res/drawable-hdpi/ic_stat_notify_' + file)
	os.system ("convert %s -resize 36x36 %s" % (file, new))
	# drawable-xhdpi
	new = ('./res/drawable-xhdpi/ic_launcher_' + file)
	os.system ("convert %s -resize 96x96 %s" % (file, new))
	new = ('./res/drawable-xhdpi/ic_stat_notify_' + file)
	os.system ("convert %s -resize 48x48 %s" % (file, new))
	
print "Complete"




