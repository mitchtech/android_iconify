#!/usr/bin/python
import os, sys

if len(sys.argv) != 2:  # the program name and image
  # stop the program and print an error message
  sys.exit("Usage: android_iconify.py icon_file_to_convert.png")

file = sys.argv[1]
if file.endswith('.png'):
	new = (os.path.splitext(file)[0] +  '_72.png')
	os.system ("convert %s -resize 72x72 %s" % (file, new))
	new = (os.path.splitext(file)[0] +  '_64.png')
	os.system ("convert %s -resize 64x64 %s" % (file, new))
	new = (os.path.splitext(file)[0] +  '_48.png')
	os.system ("convert %s -resize 48x48 %s" % (file, new))
	new = (os.path.splitext(file)[0] +  '_36.png')
	os.system ("convert %s -resize 36x36 %s" % (file, new))
	new = (os.path.splitext(file)[0] +  '_32.png')
	os.system ("convert %s -resize 32x32 %s" % (file, new))
	new = (os.path.splitext(file)[0] +  '_24.png')
	os.system ("convert %s -resize 24x24 %s" % (file, new))

print "Complete"

