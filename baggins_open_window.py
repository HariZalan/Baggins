import os
import urllib
from bagheader import *
bilbospath="/".join(os.path.realpath(__file__).split("/")[:-1])
def downloadNotify(x,fname,y):
	x.set_destination(fname)
	dialogdisplay("Download","A download has begun.")
	return True
def openWebPage(page=None,traditional=False,webv=None,name="Baggins",version="2.0",mainpage="https://zalan.withssl.com/en/baggins/mainpage_Bilbo.html",private=False,kiosk=False,title=None,autoclosable=False,boxonly=False,spinner=False,search_engine="https://duckduckgo.com/?q="):
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
		css=b"""
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
		print ("Failed to load CSS, the browser will work, but the GUI shall be poor. The exception:")
		print (e)
	if (kiosk==False):
		def searchorgo(entry,webv):
			if (entry.get_text()!="about:home"):
				url=entry.get_text()
				paersar=urllib.parse.urlparse(url)
				#paersar2=urllib.parse.urlparse("http://"+url)
				
				if (paersar.scheme):# and re.fullmatch("[abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789]*)"
					webv.load_uri(url)
				#elif (paersar2.scheme):
				#	webv.load_uri("http://"+url)
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
			webv.load_uri(search_engine+entry.get_text())
	def ourthread(entry=None,webv=WebKit2.WebView(),autoclosable=False,back=None,forward=None):
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
				if (back!=None and forward!=None):
					if (webv.can_go_back()):
						back.set_sensitive(True)
					else:
						back.set_sensitive(False)
					if (webv.can_go_forward()):
						forward.set_sensitive(True)
					else:
						forward.set_sensitive(False)
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
			
				if (kiosk==True and spinner==True):
					if (webv.is_loading()):
						spinnerr.start()
						webvbox.set_visible(False)
						spinnerbox.set_visible(True)
					else:
						spinnerr.stop()
						webvbox.set_visible(True)
						spinnerbox.set_visible(False)		
	def openinnewwindow(wv,navact,kiosk,traditional,private,title):
		x=navact.get_request().get_uri()
		openWebPage(page=x,kiosk=kiosk,traditional=traditional,private=private,title=title)
		return None
	The_third_one=Gtk.Label()
	if (kiosk==True and spinner==True):
		spinnerr=Gtk.Spinner()
		spinnerbox=Gtk.Box()
		spinnerbox.pack_end(spinnerr,expand=True,fill=True,padding=0)
		spinnerbox.set_visible(False)
	def displayuri(attercop,hittestresult,oldtomnoddy,TheThirdOne,traditional):
		if (hittestresult.context_is_link()==True):
			TheThirdOne.set_visible(True)
			TheThirdOne.set_text(WebKit2.uri_for_display(hittestresult.get_link_uri()))
		else:
			TheThirdOne.set_text("")
			if (traditional==True):
				TheThirdOne.set_visible(False)
	window=Gtk.Window()
	#window.set_icon_name("gnome-nettool")
	icon=bilbospath+"/Bilbo.png"
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
		#WebKit2.Download().connect("decide-destination",downloadNotify)
		def titlechanged(webv,unn):
			window.set_title("Baggins 2.0 “Bilbo”, the title of the current page is “"+webv.get_title()+"”")
		if (title==None):
			webv.connect("notify::title",titlechanged)
		if (private==False):
			webv.cookieManager=WebKit2.WebContext.get_default().get_cookie_manager(); WebKit2.CookieManager.set_persistent_storage(webv.cookieManager,bilbospath+"/baggins.storage",WebKit2.CookiePersistentStorage(WebKit2.CookiePersistentStorage.TEXT))
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
		#button6=Gtk.Button(label="Inspect")
		#button6.connect("clicked",lambda x: webv.get_inspector().show())
		box2.pack_start(button,expand=False,fill=False,padding=1)
		box2.pack_start(button2,expand=False,fill=False,padding=1)
		box2.pack_start(button5,expand=False,fill=False,padding=1)
		box2.pack_start(entrie,expand=True,fill=True,padding=1)
		box2.pack_start(button0,expand=False,fill=False,padding=1)
		box2.pack_start(button4,expand=False,fill=False,padding=1)
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
		webvbox=Gtk.Box()
		webvbox.pack_end(webv,expand=True,fill=True,padding=0)
		window.box.pack_end(webvbox,expand=True,fill=True,padding=0)
		if (kiosk==True and spinner==True):
			window.box.pack_end(spinnerbox,fill=False,expand=False,padding=0)
	window.add(window.box)
	window.show_all()
	if (kiosk==False):
		urlthread=threading.Thread(target=ourthread,args=(entrie,webv,autoclosable,button,button2,),daemon=True)
	else:
		urlthread=threading.Thread(target=ourthread,args=(None,webv,autoclosable,),daemon=True)
	urlthread.start()
	Gtk.main()

