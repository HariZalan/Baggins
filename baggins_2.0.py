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
if (platform.system()!="Linux"):
	print ("Warning: Baggins has been designed for Linux, so it could malfunction on thy platform.")
	if (platform.system()=="Windows"):
		print ("Sorry, Baggins will not work on Windows, even if you could compile WebKitGTK, exiting, bye.")
		exit(1)
def openWebPage(page=None,traditional=False,webv=None,name="Baggins",version="2.0",mainpage="https://zalan.withssl.com/en/baggins/mainpage_Bilbo.html",private=False,kiosk=False,title=None,autoclosable=False):
	def bookmark(webv):
		if (not os.path.exists("/".join(os.path.realpath(__file__).split("/")[:-1])+"/bookmarks.txt")):
			f=open("/".join(os.path.realpath(__file__).split("/")[:-1])+"/bookmarks.txt","w")
			f.write("")
			f.close()
		bookmarklistfile=open("/".join(os.path.realpath(__file__).split("/")[:-1])+"/bookmarks.txt")
		content=bookmarklistfile.read()#but I am not content
		content2=content.split("\n")
		if (webv.get_uri() not in content2):
			bookmarklistfile.close()
			bookmarklistfile=open("/".join(os.path.realpath(__file__).split("/")[:-1])+"/bookmarks.txt","a")
			bookmarklistfile.write(webv.get_uri()+"\n")
			bookmarklistfile.close()
		window=Gtk.Window()
		window.set_title("Your bookmarks for now")
		label=Gtk.Label()
		label.set_text(content)
		window.add(label)
		window.show_all()
		window.connect("destroy",Gtk.main_quit)
		Gtk.main()
	if (kiosk==True):
		traditional=True
	import threading
	if (page=="about:home" or page==None):
		page=mainpage
	import gi
	gi.require_version("Gtk","3.0")
	gi.require_version("WebKit2","4.0")
	from gi.repository import Gtk, WebKit2, Gdk, Gio #or WebKit2, Gtk
	try:
		css="""
		button, entry {
			border-radius: 20px;
			margin-right: 5px;
			margin-left: 5px;
		}
		.titlebutton.close:hover {
			background: red;
			transition: background 0.3s ease;
		}
		.titlebutton.close {
			transition: background 0.3s ease;
		}
		"""
		provider=Gtk.CssProvider()
		provider.load_from_data(css)
		Gtk.StyleContext.add_provider_for_screen(Gdk.Screen.get_default(),provider,Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)
	except Exception as e:
		print ("Failed to load CSS, the browser will work, but the GUI will be poor. The exception:")
		print (exception)
	if (kiosk==False):
		def searchorgo(entry,webv):
			if (entry.get_text()!="about:home"):
				url=entry.get_text()
				paersar=urllib.parse.urlparse(url)
				paersar2=urllib.parse.urlparse("http://"+url)
				
				if (paersar.scheme):# and re.fullmatch("[abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789]*)"
					webv.load_uri(url)
				elif (paersar2.scheme):
					webv.load_uri("http://"+url)
				else:
					searchuri(entry,webv)
			else:
				webv.load_uri(mainpage)
		def gotouri(entry,webv):
			if (entry.get_text()!="about:home"):
				webv.load_uri(entry.get_text())
			else:
				webv.load_uri(mainpage)
		def geturi(entry,webv):
			entry.set_text(webv.get_uri())
		def searchuri(entry,webv):
			webv.load_uri("https://google.com/search?q="+entry.get_text())
	def ourthread(entry=None,webv=WebKit2.WebView(),autoclosable=False):
		if (entry==None):
			while True:
				if (webv.get_uri().endswith("#baggins-browser-close-requested") and autoclosable==True):
					Gtk.main_quit()
		else:
			url=webv.get_uri()
			if (url!=mainpage): # Do not show URL at mainpage
				entry.set_text(url)
			else:
				entry.set_text("about:home")
			while True:
				if (webv.get_uri().endswith("#baggins-browser-close-requested") and autoclosable==True):
					Gtk.main_quit()
				if (url!=webv.get_uri()):
					if (webv.get_uri()!=mainpage): # Do not show URL at mainpage
						url=webv.get_uri()
						if (autoclosable==True and url.endswith("#baggins-browser-close-requested")):
							Gtk.main_quit()
						try:
							entry.set_text(WebKit2.uri_for_display(url))
						except:
							pass
					else:
						url=webv.get_uri()
						entry.set_text("about:home")
	def openinnewwindow(wv,navact,kiosk,traditional,private,title):
		x=navact.get_request().get_uri()
		openWebPage(page=x,kiosk=kiosk,traditional=traditional,private=private,title=title)
		return None
	The_third_one=Gtk.Label()
	def displayuri(attercop,hittestresult,oldtomnoddy,TheThirdOne,traditional):
		if (hittestresult.context_is_link()==True):
			TheThirdOne.set_visible(True)
			TheThirdOne.set_text(WebKit2.uri_for_display(hittestresult.get_link_uri()))
		else:
			TheThirdOne.set_text("")
			if (traditional==True):
				TheThirdOne.set_visible(False)
	def download(webv):
		
		fchosern=Gtk.FileChooserDialog(title="Download URI")
		fchosern.add_buttons(Gtk.STOCK_CANCEL,Gtk.ResponseType.CANCEL,Gtk.STOCK_OPEN,Gtk.ResponseType.OK)
		retriever=fchosern.run()#not labrador retriever, it is quite important
		if (retriever==Gtk.ResponseType.CANCEL):
			fchosern.destroy()
			return True
		if (retriever==Gtk.ResponseType.OK):
			filename=fchosern.get_filename()
			fchosern.destroy()
			webv.download_uri(webv.get_uri())
			WebKit2.Download.set_destination(filename,webv.Download)
			WebKit2.Download.connect("finished",lambda: print("finished"))
	window=Gtk.Window()
	#window.set_icon_name("gnome-nettool")
	icon="/".join(os.path.realpath(__file__).split("/")[:-1])+"/Bilbo.png"
	#window.set_icon("/".join(os.path.realpath(__file__).split("/")[:-1])+"/Bilbo.png")
	#icon=Gtk.IconTheme.load_icon(Gtk.IconTheme(),"3x3",Gtk.IconLookupFlags.USE_BUILTIN,None)
	if (webv==None):
		def loadfailed(webv,uri,cert,err):
			if (webv.can_go_back()==True):
				webv.load_alternate_html("""
				<!DOCTYPE html>
				<html>
					<head>
					<meta charset="utf-8"/>
					<title>Alas!</title>
					</head>
					<body style="background-color: black; text-align: center;">
					<p style="text-align: center; color: white;"><b>An error has occured while Baggins tried to load the page using HTTPS.</b></p>
					<a href="javascript:history.back()" style="color: green;">Back to the previous page</a>
					<!--<img src="https://tolkiengateway.net/w/images/a/a7/Anke_Ei%C3%9Fmann_-_The_Death_of_Isildur.jpg"/>-->
					</body>
				</html>
				""",uri,uri)
			else:
				webv.load_alternate_html("""
				<!DOCTYPE html>
				<html>
					<head>
					<meta charset="utf-8"/>
					<title>Alas!</title>
					</head>
					<body style="background-color: black; color: white; text-align: center;">
					<p style="text-align: center;"><b>An error has occured while Baggins tried to load the page using HTTPS.</b></p>
					<!--<img src="https://tolkiengateway.net/w/images/a/a7/Anke_Ei%C3%9Fmann_-_The_Death_of_Isildur.jpg"/>-->
					</body>
				</html>
				""",uri,uri)
			return True
		webv=WebKit2.WebView()
		webv.connect("create",lambda x,y: openinnewwindow(x,y,kiosk,traditional,private,title))
		webv.connect("mouse-target-changed",lambda x,y,z: displayuri(x,y,z,The_third_one,traditional))
		webv.connect("load-failed-with-tls-errors",loadfailed)
		def titlechanged(webv,unn):
			window.set_title("Baggins 2.0 “Bilbo”, the title of the current page is “"+webv.get_title()+"”")
		if (title==None):
			webv.connect("notify::title",titlechanged)
		if (private==False):
			webv.cookieManager=WebKit2.WebContext.get_default().get_cookie_manager(); WebKit2.CookieManager.set_persistent_storage(webv.cookieManager,"/".join(os.path.realpath(__file__).split("/")[:-1])+"/baggins.storage",WebKit2.CookiePersistentStorage(WebKit2.CookiePersistentStorage.TEXT))
		settings=webv.get_settings()
		WebKit2.Settings.set_user_agent_with_application_details(settings,name,version)
		#WebKit2.CookieManager.set_persistent_storage("baggins.storage")
		webv.load_uri(page)
		WebKit2.Settings.set_enable_webrtc(settings,True)
		WebKit2.Settings.set_enable_media_stream(settings,True)
		WebKit2.Settings.set_enable_developer_extras(settings,True)
		WebKit2.Settings.set_enable_back_forward_navigation_gestures(settings,True)
		WebKit2.Settings.set_default_charset(settings,"utf-8")
		#if (private==True):
		#	pass#WebKit2.Settings.set_enable_private_browsing(settings,True) deprecated
	if (kiosk==False):
		box2=Gtk.Box()
		entrie=Gtk.Entry()
		entrie.set_placeholder_text("The necessary URL or search expression")
		entrie.connect("activate",lambda x: searchorgo(entrie,webv))
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
		button6=Gtk.Button(label="⤵️")
		button6.connect("clicked",lambda x: download(webv))
		button6.set_sensitive(False)
		button7=Gtk.Button(label="📑")
		button7.connect("clicked",lambda x: bookmark(webv))
		#button6=Gtk.Button(label="Inspect")
		#button6.connect("clicked",lambda x: webv.get_inspector().show())
		box2.pack_start(button,expand=False,fill=False,padding=1)
		box2.pack_start(button2,expand=False,fill=False,padding=1)
		box2.pack_start(button5,expand=False,fill=False,padding=1)
		box2.pack_start(entrie,expand=True,fill=True,padding=1)
		box2.pack_start(button0,expand=False,fill=False,padding=1)
		box2.pack_start(button4,expand=False,fill=False,padding=1)
		box2.pack_start(button6,expand=False,fill=False,padding=1)
		box2.pack_start(button7,expand=False,fill=False,padding=1)
	#def keypressed(wget,eventitself):
	#	return False
	#box2.pack_start(button6,expand=False,fill=False,padding=1)
	window.set_size_request(1000,1000)
	if (title==None):
		window.set_title("Baggins 2.0 “Bilbo”")
	else:
		window.set_title(title)
	window.connect("destroy",Gtk.main_quit)
	#window.connect("key-press-event",keypressed)
	#window.add_accelerator(button2,"<Control>d","clicked")
	window.box=Gtk.Box(orientation=Gtk.STYLE_CLASS_VERTICAL)
	if (traditional==False):
		window.box.pack_start(webv,expand=True,fill=True,padding=0)
		if (kiosk==False):
			window.box.pack_end(box2,expand=False,fill=False,padding=0)
		window.box.pack_end(The_third_one,expand=False,fill=False,padding=0)
		if (traditional==True):
			The_third_one.set_visible(False)
	else:
		window.box.pack_end(The_third_one,expand=False,fill=False,padding=0)
		if (kiosk==False):
			window.box.pack_start(box2,expand=False,fill=False,padding=0)
		if (traditional==True):
			The_third_one.set_visible(False)
		window.box.pack_end(webv,expand=True,fill=True,padding=0)
	window.add(window.box)
	window.show_all()
	if (kiosk==False):
		urlthread=threading.Thread(target=ourthread,args=(entrie,webv,autoclosable,),daemon=True)
	else:
		urlthread=threading.Thread(target=ourthread,args=(None,webv,autoclosable,),daemon=True)
	urlthread.start()
	Gtk.main()
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
if (not os.path.exists("/".join(os.path.realpath(__file__).split("/")[:-1])+"/getget.conf.conf")):
	getgetconfconffile=open("/".join(os.path.realpath(__file__).split("/")[:-1])+"/getget.conf.conf","w")
	getgetconfconffile.write("https://zalan.withssl.com/en/baggins/get_2.0.conf")
	getgetconfconffile.close()
#locale probe
if (not os.path.exists("/".join(os.path.realpath(__file__).split("/")[:-1])+"/locales")):
	print ("Localisation file does not exist, downloading...")
	try:
		if (os.path.exists("/".join(os.path.realpath(__file__).split("/")[:-1])+"/get.conf")):
			getconf=open("/".join(os.path.realpath(__file__).split("/")[:-1])+"/get.conf")
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
	localesf=open("/".join(os.path.realpath(__file__).split("/")[:-1])+"/locales","w")
	localesf.write(ourContent)
	localesf.close()
locales=open("/".join(os.path.realpath(__file__).split("/")[:-1])+"/locales")
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
	ourFile=open("/".join(os.path.realpath(__file__).split("/")[:-1])+"/get.conf","w")
	try:
		thisContent=urllib.request.urlopen(open("/".join(os.path.realpath(__file__).split("/")[:-1])+"/getget.conf.conf").read()).read().decode()
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
if (not os.path.exists("/".join(os.path.realpath(__file__).split("/")[:-1])+"/get.conf")):
	print (localesc[2]) # print information message
	getgetconf()
getconfcontent=open("/".join(os.path.realpath(__file__).split("/")[:-1])+"/get.conf")
getconfcontent2=getconfcontent.read()
getconfcontent.close()
getconfcontent=getconfcontent2
getconfcontent=getconfcontent.split("\n")
#Check the existance of main page
if (not os.path.exists("/".join(os.path.realpath(__file__).split("/")[:-1])+"/mainpage_current.html")):
	try:
		mainpageCurrent=urllib.request.urlopen(getconfcontent[2]).read().decode()
	except Exception as ourex:
		print ("Failed to get main page:")
		print (ourex)
	else:
		mainpageCurrentf=open("/".join(os.path.realpath(__file__).split("/")[:-1])+"/mainpage_current.html","w")
		mainpageCurrentf.write(mainpageCurrent)
		mainpageCurrentf.close()
#Check the existance of Bilbo's picture.
if (not os.path.exists("/".join(os.path.realpath(__file__).split("/")[:-1])+"/Bilbo.png")):
	try:
		Bilbo=urllib.request.urlopen(getconfcontent[1]).read()
		print ("Getting the picture about Bilbo...")
	except Exception as ourex:
		print ("Failed to get the picture about Bilbo Baggins:")
		print (ourex)
	else:
		Bilbof=open("/".join(os.path.realpath(__file__).split("/")[:-1])+"/Bilbo.png","bw")
		Bilbof.write(Bilbo)
		Bilbof.close()
if (len(sys.argv)>1):
	if (arglistr.update==True):
		getgetconf()
		getconfcontent=open("/".join(os.path.realpath(__file__).split("/")[:-1])+"/get.conf")
		getconfcontent2=getconfcontent.read()
		getconfcontent.close()
		getconfcontent=getconfcontent2
		getconfcontent=getconfcontent.split("\n")
		bilbopng=urllib.request.urlopen(getconfcontent[1]).read()
		bilbopng_file=open("/".join(os.path.realpath(__file__).split("/")[:-1])+"/Bilbo.png","bw")
		bilbopng_file.write(bilbopng)
		bilbopng_file.close()
		mainpage=urllib.request.urlopen(getconfcontent[2]).read()
		mainpage_local=open("/".join(os.path.realpath(__file__).split("/")[:-1])+"/mainpage_current.html","bw")
		mainpage_local.write(mainpage)
		mainpage_local.close()
		locales=urllib.request.urlopen(getconfcontent[3]).read().decode()
		locales_local=open("/".join(os.path.realpath(__file__).split("/")[:-1])+"/locales","w")
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
		exit(0)
	if (arglistr.private==True):
		openWebPage(mainpage="file:///"+"/".join(os.path.realpath(__file__).split("/")[:-1])+"/mainpage_current.html",private=True)
		exit(0)
	if (arglistr.none==True):
		exit(0)
	if (arglistr.traditional==True):
		openWebPage(mainpage="file:///"+"/".join(os.path.realpath(__file__).split("/")[:-1])+"/mainpage_current.html",traditional=True)
		exit(0)
	if (arglistr.kiosk==True):
		url=arglistr.url
		closable=arglistr.closable
		title=arglistr.title
		openWebPage(page=url,mainpage="file:///"+"/".join(os.path.realpath(__file__).split("/")[:-1])+"/mainpage_current.html",kiosk=True,autoclosable=closable,title=title)
		exit(0)
	elif (arglistr.export==True):
		print ("Are you sure that you want to export all your logins? Your – possibly present – previous export WILL perish. Press enter to do it, ^C to exit.")
		try:
			input()
		except KeyboardInterrupt:
			exit(0)
		storage=open("/".join(os.path.realpath(__file__).split("/")[:-1])+"/baggins.storage")
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
			storage=open("/".join(os.path.realpath(__file__).split("/")[:-1])+"/baggins.storage","w")
			storage.write(toimportc)
			storage.close()
			exit(0)
	if (arglistr.url!=None):
		openWebPage(page=arglistr.url,mainpage="file:///"+"/".join(os.path.realpath(__file__).split("/")[:-1])+"/mainpage_current.html",autoclosable=arglistr.closable)
		exit(0)
else:
	openWebPage(mainpage="file:///"+"/".join(os.path.realpath(__file__).split("/")[:-1])+"/mainpage_current.html")
	exit(0)
