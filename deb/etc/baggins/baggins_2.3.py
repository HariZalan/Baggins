#!/usr/bin/env python3
import sys
import urllib.request
import urllib.parse
import os
import platform
import time
import argparse
import math
import re
import subprocess
try:
	import gi
except:
	print ("Please, install GI.")
	exit(1)
try:
	gi.require_version("Gtk","4.0")
except:
	print ("Please, install GTK 4.")
	exit(1)
from gi.repository import Gtk
path=os.path.realpath(os.path.dirname(os.path.realpath(__file__)))
fileurl="file:///"+path+"/"
bagpath=os.path.expanduser("~")+"/.baggins"
if (not os.path.exists(bagpath)):
	os.mkdir(bagpath)
if (not os.path.exists(bagpath+"/ui.css")):
	import shutil
	shutil.copyfile(path+"/ui.css",bagpath+"/ui.css")
if (platform.system()!="Linux"):
	print ("Warning: Baggins has been designed for Linux, so it might malfunction on thy platform.")
	if (platform.system()=="Windows"):
		print ("Sorry, Baggins will not work on Windows, even if you could install WebKitGTK, exiting, bye.")
		exit(1)
def wandupd(uri,file):
	try:
		OurContent=urllib.request.urlopen(uri).read()
	except Exception as Extion:
		print("Failed to update Baggins/get necessary files. To solve this, you should check your internet connection and the availability of raw.githubusercontent.com. The error message:")
		print (str(Extion))
		exit(1)
	else:
		try:
			OurFile=open(file,"bw")
			OurFile.write(OurContent)
			OurFile.close()
		except Exception as Extion:
			print ("I/O error, check the permissions, please.")
			exit(1)
from baggins_create_webview_et_al import *
argpersar=argparse.ArgumentParser()
argpersar.add_argument("-t","--traditional",action="store_true")
argpersar.add_argument("-p","--private",action="store_true")
argpersar.add_argument("-s","--setup",action="store_true")
argpersar.add_argument("-e","--export",action="store_true")
argpersar.add_argument("-i","--importdata",action="store_true")
argpersar.add_argument("-u","--update",action="store_true")
argpersar.add_argument("-k","--kiosk",action="store_true")
argpersar.add_argument("-0","--none",action="store_true")
argpersar.add_argument("-c","--closable",action="store_true")
argpersar.add_argument("-a","--createapplication",action="store_true")
argpersar.add_argument("-b","--about",action="store_true")
argpersar.add_argument("-f","--file",action="store_true")
argpersar.add_argument("url",nargs="?")
argpersar.add_argument("--title",nargs="?")
argpersar.add_argument("--aid",nargs="?")
arglistr=argpersar.parse_args()
if (not os.path.exists(bagpath+"/searchengine")):
	ourFileAgain=open(bagpath+"/searchengine","w")
	ourFileAgain.write("https://duckduckgo.com/?q=")
	ourFileAgain.close()
sEngineF=open(bagpath+"/searchengine")
sEngine=sEngineF.read()
sEngineF.close()
if (arglistr.createapplication==True):
	import baggins_create_application
	sys.exit(0)
if (arglistr.update==True):
	getgetconf()
	getconfcontent=open(path+"/get.conf")
	getconfcontent2=getconfcontent.read()
	getconfcontent.close()
	getconfcontent=getconfcontent2
	getconfcontent=getconfcontent.split("\n")
	wandupd(uri=getconfcontent[1],file=path+"/Bilbo.png")
	wandupd(uri=getconfcontent[2],file=path+"/mainpage_current.html")
	try:
		pyscriptcontent=urllib.request.urlopen(getconfcontent[0]).read().decode()
	except Exception as myException:
		print ("Failed to update Baggins. Check your internet connection and the availability of raw.githubusercontent.com. The error message:")
		print (str(myException))
	else:
		if (pyscriptcontent==""):
			print ("Something went wrong.")
		else:
			pyscriptfile=open(sys.argv[0],"w")
			pyscriptfile.write(pyscriptcontent)
			pyscriptfile.close()
			print ("The update has been completed.")
	sys.exit(0)
url=arglistr.url
if (arglistr.file==True):
	url="file://"+os.path.join(path,url)
closable=arglistr.closable
title=arglistr.title
aid=arglistr.aid
if (arglistr.export==True):
	print ("Are you sure that you want to export all your cookies? Your – possibly present – previous export WILL perish. Press enter to do it, ^C to exit.")
	try:
		input()
	except KeyboardInterrupt:
		sys.exit(0)
	storage=open(bagpath+"/.baggins.storage")
	storageContent=storage.read()
	storage.close()
	exportfile=open(os.path.expanduser("~")+"/baggins.exported","w")
	exportfile.write(storageContent)
	exportfile.close()
	sys.exit(0)
if (arglistr.importdata==True):
		print ("Are you sure that you want to import your previous cookies? Your current ones will be removed. ^C to quit, enter to proceed.")
		try:
			input()
		except KeyboardInterrupt:
			sys.exit(0)
		toimport=open(os.path.expanduser("~")+"/baggins.exported")
		toimportc=toimport.read()
		toimport.close()
		storage=open(bagpath+"/.baggins.storage","w")
		storage.write(toimportc)
		storage.close()
		sys.exit(0)
if (arglistr.setup==True):
	import baggins_setup
	sys.exit(0)
if (arglistr.about):
	import about
	sys.exit(0)
private=arglistr.private or False
if (arglistr.none==True):
	sys.exit(0)
traditional=arglistr.traditional or False
vertabbed=traditional
kiosk=arglistr.kiosk or False
openWebPage(mainpage=fileurl+"mainpage_current.html",search_engine=sEngine,private=private,page=url,autoclosable=closable,title=title,kiosk=kiosk,traditional=traditional,aid=aid,vertabbed=vertabbed)
sys.exit(0)
