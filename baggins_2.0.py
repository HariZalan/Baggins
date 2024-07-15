import sys
import urllib.request
import urllib.parse
import os
import platform
import time
import argparse
import math
import re
import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk
path="/".join(os.path.realpath(__file__).split("/")[:-1])
if (platform.system()!="Linux"):
	print ("Warning: Baggins has been designed for Linux, so it might malfunction on thy platform.")
	if (platform.system()=="Windows"):
		print ("Sorry, Baggins will not work on Windows, even if you could compile WebKitGTK, exiting, bye.")
		exit(1)
from baggins_open_window import *
def dialogdisplay(caption="Bug",text="The program has a bug, methinks."):
    ourdialog=Gtk.MessageDialog(flags=0,message_type=Gtk.MessageType.INFO,buttons=Gtk.ButtonsType.OK,text=caption)
    ourdialog.format_secondary_text(text)
    ourdialog.run()
    ourdialog.destroy()
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
	getgetconfconffile=open(path+"/getget.conf.conf","w")
	getgetconfconffile.write("https://zalan.withssl.com/en/baggins/get_2.0.conf")
	getgetconfconffile.close()
#support probe
leftsecs=1788238799-time.time()
if (leftsecs > 0 and leftsecs<=864000):
    text="The support of your version will end in "+str(leftsecs)+" seconds, what is equivalent by " + str(leftsecs/86400) + " days. Please, consider upgrading to a newer one."
    print (text)
    dialogdisplay(caption="Nearby end of support",text=text)
if (time.time()>1788238799): # September 1 2026, 04:59:59 GMT
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
	print ("get.conf does not exist, getting its content from https://zalan.withssl.com/en/baggins/get_1.0.conf...") # print information message
	getgetconf()
getconfcontent=open(path+"/get.conf")
getconfcontent2=getconfcontent.read()
getconfcontent.close()
getconfcontent=getconfcontent2
getconfcontent=getconfcontent.split("\n")
#Check the existance of main page
if (not os.path.exists(path+"/mainpage_current.html")):
	try:
		mainpageCurrent=urllib.request.urlopen(getconfcontent[2]).read().decode()
	except Exception as ourex:
		print ("Failed to get main page:")
		print (ourex)
	else:
		mainpageCurrentf=open(path+"/mainpage_current.html","w")
		mainpageCurrentf.write(mainpageCurrent)
		mainpageCurrentf.close()
#Check the existance of Bilbo's picture.
if (not os.path.exists(path+"/Bilbo.png")):
	try:
		Bilbo=urllib.request.urlopen(getconfcontent[1]).read()
		print ("Getting the picture about Bilbo...")
	except Exception as ourex:
		print ("Failed to get the picture about Bilbo Baggins:")
		print (ourex)
	else:
		Bilbof=open(path+"/Bilbo.png","bw")
		Bilbof.write(Bilbo)
		Bilbof.close()
if (len(sys.argv)>1):
	if (arglistr.update==True):
		def wandupd(uri,file):
			try:
				OurContent=urllib.request.urlopen(uri).read()
			except Exception as Extion:
				print("Failed to update Baggins. Check your internet connection and the availability of zalan.withssl.com. The error message:")
				print (str(Ei))
				exit(1)
			else:
				try:
					OurFile=open(file,"bw")
					OurFile.write(OurContent)
					OurFile.close()
				except Exception as Extion:
					print ("I/O error, check the permissions, please.")
					exit(1)
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
	if (arglistr.private==True):
		openWebPage(mainpage="file:///"+path+"/mainpage_current.html",private=True)
		exit(0)
	if (arglistr.none==True):
		exit(0)
	if (arglistr.traditional==True):
		openWebPage(mainpage="file:///"+path+"/mainpage_current.html",traditional=True)
		exit(0)
	if (arglistr.kiosk==True):
		url=arglistr.url
		closable=arglistr.closable
		title=arglistr.title
		openWebPage(page=url,mainpage="file:///"+path+"/mainpage_current.html",kiosk=True,autoclosable=closable,title=title)
		exit(0)
	elif (arglistr.export==True):
		print ("Are you sure that you want to export all your logins? Your – possibly present – previous export WILL perish. Press enter to do it, ^C to exit.")
		try:
			input()
		except KeyboardInterrupt:
			exit(0)
		storage=open(path+"/baggins.storage")
		storageContent=storage.read()
		storage.close()
		exportfile=open(os.path.expanduser("~")+"/baggins.exported","w")
		exportfile.write(storageContent)
		exportfile.close()
		exit(0)
	elif (arglistr.importdata==True):
			print ("Are you sure that you want to import your previous logins? Your current ones will be removed. ^C to quit, enter to proceed.")
			try:
				input()
			except KeyboardInterrupt:
				exit(0)
			toimport=open(os.path.expanduser("~")+"/baggins.exported")
			toimportc=toimport.read()
			toimport.close()
			storage=open(path+"/baggins.storage","w")
			storage.write(toimportc)
			storage.close()
			exit(0)
	if (arglistr.url!=None):
		openWebPage(page=arglistr.url,mainpage="file:///"+path+"/mainpage_current.html",autoclosable=arglistr.closable)
		exit(0)
else:
	openWebPage(mainpage="file:///"+path+"/mainpage_current.html")
	exit(0)
