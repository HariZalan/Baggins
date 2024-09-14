#!/usr/bin/env python3
import os
import urllib
import time
import random
bilbospath=os.path.dirname(os.path.abspath(__file__))
bagpath=os.path.expanduser("~")+"/.baggins"
import gi
gi.require_version("Gtk","3.0")
try:
	gi.require_version("WebKit2","4.1")
except:
	gi.require_version("WebKit2","4.0")
from gi.repository import Gtk, WebKit2, Gdk, Gio, GLib #or WebKit2, Gtk
from bagheader import dialogdisplay
#def downloadNotify(x,fname,y):
#	x.set_destination(fname)
#	dialogdisplay("Download","A download has begun.")
#	return True
def openWebPage2(page=None,traditional=False,webv=None,name="Baggins",version="2.0",mainpage=None,private=False,kiosk=False,title=None,autoclosable=False,boxonly=False,search_engine="https://duckduckgo.com/?q=",aid="org.freedesktop.Baggins",parent=None):
	if (aid==None):
		aid="org.freedesktop.Baggins"
	if (kiosk==True):
		traditional=True
	import threading
	if (page=="about:home" or page==None):
		page=mainpage
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
	def ourthread(entry=None,webv=WebKit2.WebView(),autoclosable=False,back=None,forward=None,reload=None):
		if (entry==None):
			while True:
				if (webv.get_uri().endswith("#baggins-browser-close-requested") and autoclosable==True):
					Gtk.main_quit()
		else:
			url=webv.get_uri()
			if (url!=mainpage): # Do not show URL at mainpage
				GLib.idle_add(lambda: entry.set_text(url))
			else:
				GLib.idle_add(lambda: entry.set_text("about:home"))
			while True:
				time.sleep(0.1)
				if (back!=None and forward!=None):
					if (webv.can_go_back()):
						GLib.idle_add(lambda: back.set_sensitive(True))
					else:
						GLib.idle_add(lambda: back.set_sensitive(False))
					if (webv.can_go_forward()):
						GLib.idle_add(lambda: forward.set_sensitive(True))
					else:
						GLib.idle_add(lambda: forward.set_sensitive(False))
				if (webv.get_uri().endswith("#baggins-browser-close-requested") and autoclosable==True):
					Gtk.main_quit()
				if (url!=webv.get_uri()):
					if (webv.get_uri()!=mainpage): # Do not show URL at mainpage
						url=webv.get_uri()
						if (autoclosable==True and url.endswith("#baggins-browser-close-requested")):
							Gtk.main_quit()
						try:
							GLib.idle_add(lambda: entry.set_text(WebKit2.uri_for_display(url)))
						except:
							pass
					else:
						url=webv.get_uri()
						GLib.idle_add(lambda: entry.set_text("about:home"))
				if (webv.is_loading() and reload!=None):
					#GLib.idle_add(reload.set_label,"🗙")
					#GLib.idle_add(reload.connect,"clicked",lambda x: webv.stop_loading())
					GLib.idle_add(lambda: reload.set_sensitive(False))
				else:
					GLib.idle_add(lambda: reload.set_sensitive(True))
				#else:
				#	GLib.idle_add(reload.set_label,"⟳")
				#	GLib.idle_add(reload.connect,"clicked",lambda x: webv.reload())
	def openinnewwindow(wv,navact,kiosk,traditional,private,title):
		x=navact.get_request().get_uri()
		openWebPage(page=x,kiosk=kiosk,traditional=traditional,private=private,title=title)
		return None
	The_third_one=Gtk.Label()
	#if (kiosk==True and spinner==True):
	#	spinnerr=Gtk.Spinner()
	#	spinnerr.set_visible(False)
	def displayuri(attercop,hittestresult,oldtomnoddy,TheThirdOne,traditional):
		if (hittestresult.context_is_link()==True):
			TheThirdOne.set_visible(True)
			TheThirdOne.set_text(WebKit2.uri_for_display(hittestresult.get_link_uri()))
		else:
			TheThirdOne.set_text("")
			if (traditional==True):
				TheThirdOne.set_visible(False)
	def goback(webv):
		def thread():
			while webv.is_loading():
				pass
			webv.go_back()
		ourThread=threading.Thread(target=thread,daemon=True)
		ourThread.start()
	def goforward(webv):
		def thread():
			while webv.is_loading():
				pass
			webv.go_back()
		ourThread=threading.Thread(target=thread,daemon=True)
		ourThread.start()
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
		def decdest(download,theroad):
			destination=theroad
			download.set_destination(GLib.filename_to_uri(os.path.expanduser("~")+"/"+"Downloads/"+destination))
			dialogdisplay("Download","Download started at ~/Downloads/"+destination)
		def downstart(session,download):
			download.connect("decide-destination",decdest)
		WebKit2.WebContext.get_default().connect("download-started",downstart)
		webv.connect("create",lambda x,y: openinnewwindow(x,y,kiosk,traditional,private,title))
		webv.connect("mouse-target-changed",lambda x,y,z: displayuri(x,y,z,The_third_one,traditional))
		webv.connect("load-failed-with-tls-errors",loadfailed)
		#WebKit2.Download().connect("decide-destination",downloadNotify)
		if (private==False):
			webv.cookieManager=WebKit2.WebContext.get_default().get_cookie_manager()
			WebKit2.CookieManager.set_persistent_storage(webv.cookieManager,bagpath+"/.baggins.storage",WebKit2.CookiePersistentStorage(WebKit2.CookiePersistentStorage.TEXT))
		settings=webv.get_settings()
		WebKit2.Settings.set_user_agent_with_application_details(settings,name,version)
		#WebKit2.CookieManager.set_persistent_storage("baggins.storage")
		webv.load_uri(page)
		WebKit2.Settings.set_enable_webrtc(settings,True)
		WebKit2.Settings.set_enable_media_stream(settings,True)
		WebKit2.Settings.set_enable_developer_extras(settings,True)
		WebKit2.Settings.set_enable_back_forward_navigation_gestures(settings,True)
		WebKit2.Settings.set_default_charset(settings,"utf-8")
		WebKit2.Settings.set_enable_caret_browsing(settings,True)
		WebKit2.Settings.set_javascript_can_access_clipboard(settings,True)
		def terminated(hight_reason):
			webv.set_alternate_html("The web process has terminated unexpectedly.")
		def cameraandmicrophone(a,b):
			if 1:
				dialogue=Gtk.MessageDialog(message_type=Gtk.MessageType.QUESTION,title="Permission request",flags=0,buttons=Gtk.ButtonsType.YES_NO)
				lambeau=Gtk.Label(label="This site wants to request a permission.")
				box=dialogue.get_content_area()
				box.add(lambeau)
				dialogue.show_all()
				responsum=dialogue.run()
				dialogue.destroy()
				if (responsum==Gtk.ResponseType.YES):
					b.allow()
				else:
					b.deny()
				return False
		#pm=WebKit2.UserMediaPermissionRequest
		#print(type(pm))
		#pm.notify()
		webv.connect("permission-request", cameraandmicrophone)
		webv.connect("web-process-terminated",terminated)
		#if (private==True):
		#	pass#WebKit2.Settings.set_enable_private_browsing(settings,True) deprecated
	if (kiosk==False):
		box2=Gtk.Box()
		entrie=Gtk.Entry()
		entrie.set_placeholder_text("The necessary URL or search expression")
		entrie.connect("activate",lambda x: searchorgo(entrie,webv))
		button0=Gtk.Button(label="Go")
		button0.connect("clicked",lambda x: gotouri(entrie,webv))
		button=Gtk.Button()
		button.add(Gtk.Arrow(arrow_type=Gtk.ArrowType.LEFT,shadow_type=Gtk.ShadowType.NONE))
		button.connect("clicked",lambda x: goback(webv))
		button2=Gtk.Button()
		button2.add(Gtk.Arrow(arrow_type=Gtk.ArrowType.RIGHT,shadow_type=Gtk.ShadowType.NONE))
		button2.connect("clicked",lambda x: goforward(webv))
		button4=Gtk.Button.new_from_icon_name("system-search-symbolic",Gtk.IconSize.MENU)
		button4.connect("clicked", lambda x: searchuri(entrie,webv))
		button5=Gtk.Button.new_from_icon_name("view-refresh-symbolic",Gtk.IconSize.MENU)
		button5.connect("clicked",lambda x: webv.reload())
		button6=Gtk.Button.new_from_icon_name("folder-download-symbolic",Gtk.IconSize.MENU)
		button6.connect("clicked",lambda x: webv.save_to_file(Gio.File.new_for_path(os.path.expanduser("~")+"/Downloads/"+str(random.randrange(10000))+".mhtml"),WebKit2.SaveMode(0),None,None,None))
		#button6=Gtk.Button(label="Inspect")
		#button6.connect("clicked",lambda x: webv.get_inspector().show())
		box2.pack_start(button,expand=False,fill=False,padding=1)
		box2.pack_start(button2,expand=False,fill=False,padding=1)
		box2.pack_start(button5,expand=False,fill=False,padding=1)
		box2.pack_start(entrie,expand=True,fill=True,padding=1)
		box2.pack_start(button0,expand=False,fill=False,padding=1)
		box2.pack_start(button4,expand=False,fill=False,padding=1)
		box2.pack_start(button6,expand=False,fill=False,padding=1)
	#def keypressed(wget,eventitself):
	#	return False
	#box2.pack_start(button6,expand=False,fill=False,padding=1)
	#window.connect("key-press-event",keypressed)
	#window.add_accelerator(button2,"<Control>d","clicked")
	box=Gtk.Box(orientation=Gtk.STYLE_CLASS_VERTICAL)
	if (traditional==False):
		box.pack_start(webv,expand=True,fill=True,padding=0)
		if (kiosk==False):
			box.pack_end(box2,expand=False,fill=False,padding=0)
		box.pack_end(The_third_one,expand=False,fill=False,padding=0)
		if (traditional==True):
			The_third_one.set_visible(False)
	else:
		box.pack_end(The_third_one,expand=False,fill=False,padding=0)
		if (kiosk==False):
			box.pack_start(box2,expand=False,fill=False,padding=0)
		if (traditional==True):
			The_third_one.set_visible(False)
		webvbox=Gtk.Box()
		webvbox.pack_end(webv,expand=True,fill=True,padding=0)
		box.pack_end(webvbox,expand=True,fill=True,padding=0)
		#if (kiosk==True and spinner==True):
		#	box.pack_end(spinnerr,fill=True,expand=False,padding=0)
	#nb=Gtk.Notebook()
	#nb.new()
	#nb.append_page(box)
	#window.add(nb)
	if (kiosk==False):
		urlthread=threading.Thread(target=ourthread,args=(entrie,webv,autoclosable,button,button2,button5,),daemon=True)
	else:
		urlthread=threading.Thread(target=ourthread,args=(None,webv,autoclosable,),daemon=True)
	urlthread.start()
	#box.set_parent(parent) if parent else False
	return box
def openWebPage(page=None,traditional=False,name="Baggins",version="2.0",mainpage=None,private=False,kiosk=False,title=None,autoclosable=False,boxonly=False,search_engine="https://duckduckgo.com/?q=",aid=None,tabbed=False):
	window=Gtk.Window()
	box=openWebPage2(page=page,traditional=traditional,name=name,version=version,mainpage=mainpage,private=private,kiosk=kiosk,autoclosable=autoclosable,search_engine=search_engine,aid=aid)
	if not kiosk:
		tabbed=True
	if (tabbed):
		nb=Gtk.Notebook()
		nb.new()
		def newtab(x):
			#GLib.idle_add(lambda: nb.append_page(openWebPage2(page=page, traditional=traditional, name=name, version=version, mainpage=mainpage, private=private, kiosk=kiosk, autoclosable=autoclosable, search_engine=search_engine, aid=aid,parent=nb)))
			nb.append_page(openWebPage2(page=page, traditional=traditional, name=name, version=version, mainpage=mainpage, private=private, kiosk=kiosk, autoclosable=autoclosable, search_engine=search_engine, aid=aid,parent=nb))
			nb.show_all()
		nb.append_page(box)
		window.add(nb)
		b=Gtk.Button.new_from_icon_name("tab-new",Gtk.IconSize.MENU)
		b.connect("clicked",newtab)
		hb=Gtk.HeaderBar()
		hb.set_show_close_button(True)
		hb.pack_start(b)
		window.set_titlebar(hb)
	else:
		window.add(box)
	window.set_default_size(1000,1000)
	GLib.set_prgname(aid or "org.freedesktop.Baggins")
	window.set_title(title or "Baggins 2.1 “Balin Fundin’s son”")
	window.show_all()
	window.connect("destroy",Gtk.main_quit)
	Gtk.main()
