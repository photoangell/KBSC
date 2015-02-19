#!/usr/bin/python
import socket
import urllib2
#import webbrowser
import os
import glob

from datetime import datetime

d = datetime.utcnow()

picture_page = "http://www.tfl.gov.uk/tfl/livetravelnews/trafficcams/cctv/0000106710.jpg"
# timeout in seconds
timeout = 180
socket.setdefaulttimeout(timeout)

#webbrowser.open(picture_page)  # test
# open the web page picture and read it into a variable
# **need to wrap this in a try loop
opener1 = urllib2.build_opener()
page1 = opener1.open(picture_page)
my_picture = page1.read()

#compare with most recent file.
os.chdir("/home/shonen/KBSC")
#change dir
newdir = d.strftime("%Y_%m_%d")

if not(os.path.exists(newdir)):
	os.mkdir (newdir)

os.chdir(newdir)

filelist = []

for files in glob.glob("KBSC_*.*"):
	#print files
	filelist.append(files)

oldpic = ""
if len(filelist) > 0:
	newest = max(filelist)
	#print filen
	fin = open(newest, "rb")
	oldpic = fin.read()
	fin.close()

if (oldpic != my_picture): # or (len(filelist) == 0):
	# open file for binary write and save picture
	# picture_page[-4:] extracts extension eg. .gif
	# (most image file extensions have three letters, otherwise modify)
	filename = "KBSC_" + d.strftime("%Y_%m_%d_%H_%M_%S") + ".jpg"
	#+ picture_page[-4:]

	#print filename  # test
	fout = open(filename, "wb")
	fout.write(my_picture)
	fout.close()
	# was it saved correctly?
	# test it out ...
	#webbrowser.open(filename)
	# or ...
	# on Windows this will display the image in the default viewer
	#os.startfile(filename)
#else:
#	print "file is same"




