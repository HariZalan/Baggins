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
try:
	import gi
except:
	print ("Please, install GI.")
	exit(1)
try:
	gi.require_version("Gtk","3.0")
except:
	print ("Please, install GTK 3.")
from gi.repository import Gtk
path="/".join(os.path.realpath(__file__).split("/")[:-1])
fileurl="file:///"+path+"/"
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
try:
	from bagheader import *
except:
	wandupd("https://raw.githubusercontent.com/HariZalan/Baggins/2.0-alpha/bagheader.py","bagheader.py")
	from bagheader import *
try:
	from baggins_open_window import *
except:
	wandupd("https://raw.githubusercontent.com/HariZalan/Baggins/2.0-alpha/baggins_open_window.py","baggins_open_window.py")
	from baggins_open_window import *
argpersar=argparse.ArgumentParser()
argpersar.add_argument("-t","--traditional",action="store_true")
argpersar.add_argument("-p","--private",action="store_true")
argpersar.add_argument("-e","--export",action="store_true")
argpersar.add_argument("-i","--importdata",action="store_true")
argpersar.add_argument("-u","--update",action="store_true")
argpersar.add_argument("-k","--kiosk",action="store_true")
argpersar.add_argument("-0","--none",action="store_true")
argpersar.add_argument("-c","--closable",action="store_true")
argpersar.add_argument("url",nargs="?")
argpersar.add_argument("--title",nargs="?")
arglistr=argpersar.parse_args()
#getgetconfconf
if (not os.path.exists(path+"/getget.conf.conf")):
	wandupd(uri="https://raw.githubusercontent.com/HariZalan/Baggins/2.0-alpha/getget.conf.conf",file=path+"/getget.conf.conf")
#support probe
endofsupport=1788238799
leftsecs=endofsupport-time.time()
if (leftsecs > 0 and leftsecs<=864000):
    text="The support of your version will end in "+str(leftsecs)+" seconds, what is equivalent by " + str(leftsecs/86400) + " days. Please, consider upgrading to a newer one."
    print (text)
    dialogdisplay(caption="Nearby end of support",text=text)
if (time.time()>endofsupport): # September 1 2026, 04:59:59 GMT
	text="Your current Baggins version is not supported, please, upgrade to a newer one. You can run Baggins with -u to do this."
	print (text)
	dialogdisplay(caption="The support ended",text=text)
	if (time.time()>1797832799): # December 21 2025, 05:59:59 GMT
		if (not os.path.exists("IWillUpgradeIPromise")):
			text="(Y)our version is extremely old, create IWillUpgradeIPromise at /etc/baggins to run it."
			print (text)
			dialogdisplay(caption="Extremely eld version",text=text)
			exit (1)
#Function
def getgetconf():
	global localesc
	ourFile=open(path+"/get.conf","w")
	try:
		thisContent=urllib.request.urlopen(open(path+"/getget.conf.conf").read()).read().decode()
	except Exception as MyException:
		print ("Something went wrong. If you think that it is a bug, contact me at either harizalan12@gmail.com or harizalan.programs@gmail.com. "+str(MyException))# print error message
		ourFile.close()
	else:
		if (thisContent!=""):
			ourFile.write(thisContent)
			ourFile.close()
			print ("Completed!")
		else:
			print ("")
#get.conf probe
if (not os.path.exists(path+"/get.conf")):
	print ("get.conf does not exist, getting its content...") # print information message
	getgetconf()
getconfcontent=open(path+"/get.conf")
getconfcontent2=getconfcontent.read()
getconfcontent.close()
getconfcontent=getconfcontent2
getconfcontent=getconfcontent.split("\n")
#Check the existance of main page
if (not os.path.exists(path+"/mainpage_current.html")):
	wandupd(getconfcontent[2],path+"/mainpage_current.html")
#Check the existance of Bilbo's picture.
if (not os.path.exists(path+"/Bilbo.png")):
	wandupd(getconfcontent[1],path+"/Bilbo.png")
if (not os.path.exists(path+"/searchengine")):
	ourFileAgain=open("searchengine","w")
	ourFileAgain.write("https://duckduckgo.com/?q=")
	ourFileAgain.close()
if (not os.path.exists(path+"/baggins_setup.py")):
	wandupd("https://raw.githubusercontent.com/HariZalan/Baggins/2.0-alpha/baggins_setup.py",path+"/baggins_setup.py")
sEngineF=open(path+"/searchengine")
sEngine=sEngineF.read()
sEngineF.close()
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
		print ("Failed to update Baggins. Check your internet connection and the availability of zalan.withssl.com. The error message:")
		print (str(myException))
	else:
		if (pyscriptcontent==""):
			print ("Something went wrong.")
		else:
			pyscriptfile=open(sys.argv[0],"w")
			pyscriptfile.write(pyscriptcontent)
			pyscriptfile.close()
			print ("The update has been completed.")
	exit(0)
url=arglistr.url
closable=arglistr.closable
title=arglistr.title
if (arglistr.private==True):
	private=True	#openWebPage(mainpage=fileurl+"mainpage_current.html",private=True,search_engine=sEngine)
else:
	private=False
if (arglistr.none==True):
	exit(0)
if (arglistr.traditional==True):
	traditional=True	#openWebPage(mainpage=fileurl+"mainpage_current.html",traditional=True,search_engine=sEngine)
else:
	traditional=False
if (arglistr.kiosk==True):
	kiosk=True
else:
	kiosk=False
	#openWebPage(page=url,mainpage=fileurl+"mainpage_current.html",kiosk=True,autoclosable=closable,title=title,search_engine=sEngine)
if (arglistr.export==True):
	print ("Are you sure that you want to export all your cookies? Your – possibly present – previous export WILL perish. Press enter to do it, ^C to exit.")
	try:
		input()
	except KeyboardInterrupt:
		exit(0)
	storage=open(os.path.expanduser("~")+"/.baggins.storage")
	storageContent=storage.read()
	storage.close()
	exportfile=open(os.path.expanduser("~")+"/baggins.exported","w")
	exportfile.write(storageContent)
	exportfile.close()
	exit(0)
if (arglistr.importdata==True):
		print ("Are you sure that you want to import your previous cookies? Your current ones will be removed. ^C to quit, enter to proceed.")
		try:
			input()
		except KeyboardInterrupt:
			exit(0)
		toimport=open(os.path.expanduser("~")+"/baggins.exported")
		toimportc=toimport.read()
		toimport.close()
		storage=open(os.path.expanduser("~")+"/.baggins.storage","w")
		storage.write(toimportc)
		storage.close()
		exit(0)
openWebPage(mainpage=fileurl+"mainpage_current.html",search_engine=sEngine,private=private,page=url,autoclosable=closable,title=title,kiosk=kiosk,traditional=traditional)
exit(0)
