import sys
import urllib.request
import os
import time
def openWebPage(page):
	import threading
	import gi
	gi.require_version("Gtk","3.0")
	gi.require_version("WebKit2","4.0")
	from gi.repository import Gtk, WebKit2 #or WebKit2, Gtk
	def gotouri(entry,webv):
		webv.load_uri(entry.get_text())
	def geturi(entry,webv):
		entry.set_text(webv.get_uri())
	def searchuri(entry,webv):
		webv.load_uri("https://google.com/search?q="+entry.get_text())
	def ourthread(entry,webv):
		#mydogisnotsuicide=hurray
		url=webv.get_uri()
		if (url!="https://zalan.withssl.com/en/baggins/mainpage_Bilbo.html"):
			entry.set_text(url)
		while True:
			if (url!=webv.get_uri()):
				url=webv.get_uri()
				entry.set_text(url)
	webv=WebKit2.WebView()
	webv.load_uri(page)
	#WebKit2.Settings.set_enable_webrtc(WebKit2.Settings(),True)
	box2=Gtk.Box()
	entrie=Gtk.Entry()
	entrie.set_placeholder_text("The necessary URL or search expression")
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
	box2.pack_start(button,expand=False,fill=False,padding=1)
	box2.pack_start(button2,expand=False,fill=False,padding=1)
	box2.pack_start(button5,expand=False,fill=False,padding=1)
	box2.pack_start(entrie,expand=True,fill=True,padding=1)
	box2.pack_start(button0,expand=False,fill=False,padding=1)
	box2.pack_start(button4,expand=False,fill=False,padding=1)
	window=Gtk.Window()
	window.set_size_request(1000,1000)
	window.set_title("Baggins 2.0 “Bilbo”")
	window.connect("destroy",Gtk.main_quit)
	window.box=Gtk.Box(orientation=Gtk.STYLE_CLASS_VERTICAL)
	window.box.pack_start(webv,expand=True,fill=True,padding=0)
	window.box.pack_end(box2,expand=False,fill=False,padding=0)
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
	print ("Your current Baggins version is not supported, please, upgrade to a newer one. You can run Baggins with -U and then -u to do this.")
	window=tk.Tk()
	window.title("The support ended")
	tk.Label(window,text="Your current Baggins version is not supported, please, upgrade to a newer one. You can run Baggins with -U and then -u to do this.").pack()
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
		openWebPage("https://zalan.withssl.com/en/baggins/mainpage_Bilbo.html")
	elif (sys.argv[1]=="--none" or sys.argv[1]=="-0"):
		exit(0)
	else:
		openWebPage(sys.argv[1])
else:
	openWebPage("https://zalan.withssl.com/en/baggins/mainpage_Bilbo.html")