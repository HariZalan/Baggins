#!/usr/bin/env python3
import sys
import urllib.request
import os
import time
import argparse
def openWebPage(page="thereiswebview",traditional=False,webv=None,name="Baggins",version="2.0",mainpage="https://zalan.withssl.com/en/baggins/mainpage_Bilbo.html",private=False):
	import threading
	if (page=="about:home"):
		page=mainpage
	import gi
	gi.require_version("Gtk","3.0")
	gi.require_version("WebKit2","4.0")
	from gi.repository import Gtk, WebKit2, Gdk #or WebKit2, Gtk
	def gotouri(entry,webv):
		if (entry.get_text()!="about:home"):
			webv.load_uri(entry.get_text())
		else:
			webv.load_uri(mainpage)
	def geturi(entry,webv):
		entry.set_text(webv.get_uri())
	def searchuri(entry,webv):
		webv.load_uri("https://google.com/search?q="+entry.get_text())
	def ourthread(entry,webv):
		url=webv.get_uri()
		if (url!=mainpage): # Do not show URL at mainpage
			entry.set_text(url)
		else:
			entry.set_text("about:home")
		while True:
			if (url!=webv.get_uri()):
				if (webv.get_uri()!=mainpage): # Do not show URL at mainpage
					url=webv.get_uri()
					entry.set_text(url)
				else:
					url=webv.get_uri()
					entry.set_text("about:home")
	def openinnewwindow(wv,navact):
		x=navact.get_request().get_uri()
		openWebPage(page=x)
		return None
	The_third_one=Gtk.Label()
	def displayuri(attercop,hittestresult,oldtomnoddy,TheThirdOne):
		if (hittestresult.context_is_link()==True):
			TheThirdOne.set_visible(True)
			TheThirdOne.set_text(hittestresult.get_link_uri())
		else:
			TheThirdOne.set_text("")
			TheThirdOne.set_visible(False)
	window=Gtk.Window()
	if (webv==None):
		webv=WebKit2.WebView()
		webv.connect("create",openinnewwindow)
		webv.connect("mouse-target-changed",lambda x,y,z: displayuri(x,y,z,The_third_one))
		def titlechanged(a,b,title,webv):
			window.set_title("Baggins 2.0 “Bilbo”, "+webv.get_uri()+" is opened, title: "+title)
		#webv.connect("title-changed",lambda x, y, z: titlechanged(x,y,z,webv))
		if (private==False):
			webv.cookieManager=WebKit2.WebContext.get_default().get_cookie_manager(); WebKit2.CookieManager.set_persistent_storage(webv.cookieManager,"baggins.storage",WebKit2.CookiePersistentStorage(WebKit2.CookiePersistentStorage.TEXT))
		settings=webv.get_settings()
		WebKit2.Settings.set_user_agent_with_application_details(settings,name,version)
		#WebKit2.CookieManager.set_persistent_storage("baggins.storage")
		webv.load_uri(page)
		#WebKit2.Settings.set_enable_webrtc(settings,True)
	box2=Gtk.Box()
	entrie=Gtk.Entry()
	entrie.set_placeholder_text("The necessary URL or search expression")
	entrie.connect("activate",lambda x: gotouri(entrie,webv))
	button0=Gtk.Button(label="Go")
	button0.connect("clicked",lambda x: gotouri(entrie,webv))
	button=Gtk.Button(label="←")
	button.connect("clicked",lambda x: webv.go_back())
	button2=Gtk.Button(label="→")
	button2.connect("clicked",lambda x: webv.go_forward())
	button4=Gtk.Button(label="🔍")
	button4.connect("clicked", lambda x: searchuri(entrie,webv))
	button5=Gtk.Button(label="⟳")
	button5.connect("clicked",lambda x: webv.reload())
	#button6=Gtk.Button(label="Inspect")
	#button6.connect("clicked",lambda x: webv.get_inspector().show())
	box2.pack_start(button,expand=False,fill=False,padding=1)
	box2.pack_start(button2,expand=False,fill=False,padding=1)
	box2.pack_start(button5,expand=False,fill=False,padding=1)
	box2.pack_start(entrie,expand=True,fill=True,padding=1)
	box2.pack_start(button0,expand=False,fill=False,padding=1)
	box2.pack_start(button4,expand=False,fill=False,padding=1)
	#box2.pack_start(button6,expand=False,fill=False,padding=1)
	window.set_size_request(1000,1000)
	window.set_title("Baggins 2.0 “Bilbo”")
	window.connect("destroy",Gtk.main_quit)
	accelerator_nottooquick=Gtk.AccelGroup()
	accelerator_nottooquick.connect(Gdk.keyval_from_name("b"),Gdk.ModifierType.CONTROL_MASK,0,lambda x,y,z,w: webv.go_back())
	window.add_accel_group(accelerator_nottooquick)
	accelerator_nottooquick_second=Gtk.AccelGroup()
	accelerator_nottooquick_second.connect(Gdk.keyval_from_name("d"),Gdk.ModifierType.CONTROL_MASK,0,lambda x,y,z,w: webv.go_forward())
	window.add_accel_group(accelerator_nottooquick_second)
	window.box=Gtk.Box(orientation=Gtk.STYLE_CLASS_VERTICAL)
	if (traditional==False):
		window.box.pack_start(webv,expand=True,fill=True,padding=0)
		window.box.pack_end(box2,expand=False,fill=False,padding=0)
		window.box.pack_end(The_third_one,expand=False,fill=False,padding=0)
	else:
		window.box.pack_start(box2,expand=False,fill=False,padding=0)
		window.box.pack_end(The_third_one,expand=False,fill=False,padding=0)
		window.box.pack_end(webv,expand=True,fill=True,padding=0)
	window.add(window.box)
	window.show_all()
	urlthread=threading.Thread(target=ourthread,args=(entrie,webv,),daemon=True)
	urlthread.start()
	Gtk.main()
try:
	import tkinter as tk
except:
	print ("Tkinter is not installed. The script installs it, but you will need to run Baggins again.")
	import subprocess
	try:
		subprocess.run("pip install tkinter",shell=True)
	except Exception as ourEczema:
		print ("Argh. It failed as well. On Ubuntu/Debian, the environment can be externally managed, and you will need to install Tkinter with either sudo apt install python3-tkinter or sudo apt install python-tkinter. The exception:")
		print (ourEczema)
#getgetconfconf
if (not os.path.exists("./getget.conf.conf")):
	getgetconfconffile=open("getget.conf.conf","w")
	getgetconfconffile.write("https://zalan.withssl.com/en/baggins/get_2.0.conf")
	getgetconfconffile.close()
#locale probe
if (not os.path.exists("./locales")):
	print ("Localisation file does not exist, downloading...")
	try:
		if (os.path.exists("./get.conf")):
			getconf=open("get.conf")
			getconfcontent=getconf.read()
			getconf.close()
			getconfcontent=getconfcontent.split("\n")
			ourContent=urllib.request.urlopen(getconfcontent[3]).read().decode()				
		else:
			ourContent=urllib.request.urlopen("https://zalan.withssl.com/en/baggins/locales_en_2.0").read().decode()
	except Exception as ourex:
		print ("Failed, exiting.")
		print (ourex)
		exit (1)
	localesf=open("./locales","w")
	localesf.write(ourContent)
	localesf.close()
locales=open("./locales")
localesc=locales.read()
locales.close()
localesc=localesc.replace("\n","")
localesc=localesc.split("SEPARATOR")
#support probe
leftsecs=1788238799-time.time()
if (leftsecs > 0 and leftsecs<=864000):
	print ("The support of your version will end in "+str(leftsecs)+" seconds, what is equivalent by " + str(leftsecs/86400) + " days. Please, consider upgrading to a newer one.")
	window=tk.Tk()
	window.title("The end of support is near")
	labelle=tk.Label(window,text="The support of your version will end in  "+str(leftsecs)+" seconds, what is equivalent by "+str(leftsecs/86400)+" days. Please, consider upgrading to a newer one. Close this window to proceed.")
	labelle.pack()
	window.mainloop()
if (time.time()>1788238799): # September 1 2026, 04:59:59 GMT
	print ("Your current Baggins version is not supported, please, upgrade to a newer one. You can run Baggins with -u to do this.")
	window=tk.Tk()
	window.title("The support ended")
	tk.Label(window,text="Your current Baggins version is not supported, please, upgrade to a newer one. You can run Baggins with -u to do this.").pack()
	window.mainloop()
	if (time.time()>1797832799): # December 21 2025, 05:59:59 GMT
		if (not os.path.exists("IWillUpgradeIPromise")):
			print ("Your version is extremely old, create IWillUpgradeIPromise to run Baggins.")
			window=tk.Tk()
			window.title("Extremely old version")
			tk.Label(window,text="Your version is extremely old, create file IWillUpgradeIPromise in the folder of Baggins to run it.").pack()
			window.mainloop()
			exit (1)
#Function
def getgetconf():
	global localesc
	ourFile=open("./get.conf","w")
	try:
		thisContent=urllib.request.urlopen(open("getget.conf.conf").read()).read().decode()
	except Exception as MyException:
		print (localesc[0]+str(MyException))# print error message
		ourFile.close()
	else:
		if (thisContent!=""):
			ourFile.write(thisContent)
			ourFile.close()
			print (localesc[1])
		else:
			print ("")
#get.conf probe
if (not os.path.exists("./get.conf")):
	print (localesc[2]) # print information message
	getgetconf()
getconfcontent=open("./get.conf")
getconfcontent2=getconfcontent.read()
getconfcontent.close()
getconfcontent=getconfcontent2
getconfcontent=getconfcontent.split("\n")
#Check the existance of main page
if (not os.path.exists("./mainpage_current.html")):
	try:
		mainpageCurrent=urllib.request.urlopen(getconfcontent[2]).read().decode()
	except Exception as ourex:
		print ("Failed to get main page:")
		print (ourex)
	else:
		mainpageCurrentf=open("./mainpage_current.html","w")
		mainpageCurrentf.write(mainpageCurrent)
		mainpageCurrentf.close()
#Check the existance of Bilbo's picture.
if (not os.path.exists("./Bilbo.png")):
	try:
		Bilbo=urllib.request.urlopen(getconfcontent[1]).read()
		print ("Getting the picture about Bilbo...")
	except Exception as ourex:
		print ("Failed to get the picture about Bilbo Baggins:")
		print (ourex)
	else:
		Bilbof=open("./Bilbo.png","bw")
		Bilbof.write(Bilbo)
		Bilbof.close()
if (len(sys.argv)==2):
	if (sys.argv[1]=="-h" or sys.argv[1]=="--help"):
		print (localesc[5])
	elif (sys.argv[1]=="-u" or sys.argv[1]=="--upgrade"):
		getgetconf()
		getconfcontent=open("./get.conf")
		getconfcontent2=getconfcontent.read()
		getconfcontent.close()
		getconfcontent=getconfcontent2
		getconfcontent=getconfcontent.split("\n")
		bilbopng=urllib.request.urlopen(getconfcontent[1]).read()
		bilbopng_file=open("Bilbo.png","bw")
		bilbopng_file.write(bilbopng)
		bilbopng_file.close()
		mainpage=urllib.request.urlopen(getconfcontent[2]).read()
		mainpage_local=open("./mainpage_current.html","bw")
		mainpage_local.write(mainpage)
		mainpage_local.close()
		locales=urllib.request.urlopen(getconfcontent[3]).read().decode()
		locales_local=open("locales","w")
		locales_local.write(locales)
		locales_local.close()
		print (localesc[6])
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
				print (localesc[7])
	elif (sys.argv[1]=="-p" or sys.argv[1]=="--private"):
		openWebPage("https://zalan.withssl.com/en/baggins/mainpage_Bilbo.html",private=True)
	elif (sys.argv[1]=="--none" or sys.argv[1]=="-0"):
		exit(0)
	elif (sys.argv[1]=="--traditional" or sys.argv[1]=="-t"):
		openWebPage("https://zalan.withssl.com/en/baggins/mainpage_Bilbo.html",traditional=True)
	else:
		openWebPage(sys.argv[1])
else:
	openWebPage("https://zalan.withssl.com/en/baggins/mainpage_Bilbo.html")
