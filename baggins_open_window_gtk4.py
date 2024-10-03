#!/usr/bin/env python3
import os
import urllib
import time
import random
bilbospath=os.path.realpath(os.path.dirname(os.path.realpath(__file__)))
bagpath=os.path.expanduser("~")+"/.baggins"
import gi
gi.require_version("Gtk","4.0")
gi.require_version("WebKit","6.0")
from gi.repository import Gtk, Gdk, Gio, GLib
from gi.repository import WebKit as WebKit2
#from bagheader import dialogdisplay
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
		/*@binding-set NewTab {
			bind "<Control>T" { "newtab" };
		}*/
		notebook {
			transition: background 0.5s ease;
			/*-gtk-key-bindings: NewTab;*/
		}
		notebook.header {
			border: none;
		}
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
		Gtk.StyleContext.add_provider_for_display(Gdk.Display.get_default(),provider,Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)
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
	def ourthread(entry=None,webv=WebKit2.WebView(),autoclosable=False,back=None,forward=None,reload=None,box=None):
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
			webv.go_forward()
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
		webv.set_size_request(1000,900)
		webv.set_hexpand(True)
		webv.set_vexpand(True)
		def decdest(download,theroad):
			destination=theroad
			download.set_destination(GLib.filename_to_uri(os.path.expanduser("~")+"/"+"Downloads/"+destination))
			dialogdisplay("Download","Download started at ~/Downloads/"+destination)
		def downstart(session,download):
			download.connect("decide-destination",decdest)
		#WebKit2.WebContext.get_default().connect("download-started",downstart)
		webv.connect("create",lambda x,y: openinnewwindow(x,y,kiosk,traditional,private,title))
		webv.connect("mouse-target-changed",lambda x,y,z: displayuri(x,y,z,The_third_one,traditional))
		webv.connect("load-failed-with-tls-errors",loadfailed)
		#WebKit2.Download().connect("decide-destination",downloadNotify)
		if (private==False):
			webv.cookieManager=WebKit2.NetworkSession.get_default().get_cookie_manager()
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
			webv.load_alternate_html("""The web process has terminated unexpectedly<p><i>Clap! Snap! the black crack!
Grip, grab! Pinch, nab!<br/>
And down down to Goblin-town<br/>
    You go, my lad!<br/><br/>

Clash, crash! Crush, smash!<br/>
Hammer and tongs! Knocker and gongs!<br/>
Pound, pound, far underground!<br/>
     Ho, ho! my lad!<br/><br/>

Swish, smack! Whip crack!<br/>
Batter and beat! Yammer and bleat!<br/>
Work, work! Nor dare to shirk,<br/>
While Goblins quaff, and Goblins laugh,<br/>
Round and round far underground<br/>
     Below, my lad</i><br/><br/> The Hobbit, J. R. R. Tolkien</p>""",webv.get_uri(),webv.get_uri())
		def cameraandmicrophone(a,b):
			if 1:
				dialogue=Gtk.MessageDialog(message_type=Gtk.MessageType.QUESTION,title="Permission request",flags=0,buttons=Gtk.ButtonsType.YES_NO)
				lambeau=Gtk.Label(label="This site wants to request a permission.")
				box=dialogue.get_content_area()
				box.set_child(lambeau)
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
		webv.connect("web-process-terminated",lambda x,y: terminated(x))
		#if (private==True):
		#	pass#WebKit2.Settings.set_enable_private_browsing(settings,True) deprecated
	if (kiosk==False):
		box2=Gtk.Box()
		entrie=Gtk.Entry()
		entrie.set_placeholder_text("The necessary URL or search expression")
		entrie.connect("activate",lambda x: searchorgo(entrie,webv))
		button0=Gtk.Button(label="Go")
		button0.connect("clicked",lambda x: gotouri(entrie,webv))
		button=Gtk.Button.new_from_icon_name("go-previous-symbolic")
		button.connect("clicked",lambda x: goback(webv))
		button2=Gtk.Button.new_from_icon_name("go-next-symbolic")
		button2.connect("clicked",lambda x: goforward(webv))
		button4=Gtk.Button.new_from_icon_name("system-search-symbolic")
		button4.connect("clicked", lambda x: searchuri(entrie,webv))
		button5=Gtk.Button.new_from_icon_name("view-refresh-symbolic")
		button5.connect("clicked",lambda x: webv.reload())
		button6=Gtk.Button.new_from_icon_name("folder-download-symbolic")
		button6.connect("clicked",lambda x: webv.save_to_file(Gio.File.new_for_path(os.path.expanduser("~")+"/Downloads/"+str(random.randrange(10000))+".mhtml"),WebKit2.SaveMode(0),None,None,None))
		#button6=Gtk.Button(label="Inspect")
		#button6.connect("clicked",lambda x: webv.get_inspector().show())
		box2.append(button)
		box2.append(button2)
		box2.append(button5)
		box2.append(entrie)
		box2.append(button0)
		box2.append(button4)
		box2.append(button6)
	#def keypressed(wget,eventitself):
	#	return False
	#box2.append(button6)
	#window.connect("key-press-event",keypressed)
	#window.add_accelerator(button2,"<Control>d","clicked")
	box=Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
	if (traditional==True):
		box.append(webv)
		if (kiosk==False):
			box.prepend(box2)
		box.prepend(The_third_one)
		if (traditional==True):
			The_third_one.set_visible(False)
	else:
		box.prepend(The_third_one)
		if (kiosk==False):
			box.append(box2)
		if (traditional==True):
			The_third_one.set_visible(False)
		webvbox=Gtk.Box()
		webvbox.prepend(webv)
		box.prepend(webvbox)
	if(box!=None):
		box.title=webv.get_title()
		#if (kiosk==True and spinner==True):
		#	box.prepend(spinnerr,fill=True,expand=False,padding=0)
	#nb=Gtk.Notebook()
	#nb.new()
	#nb.append_page(box)
	#window.add(nb)
	if (kiosk==False):
		urlthread=threading.Thread(target=ourthread,args=(entrie,webv,autoclosable,button,button2,button5,box,),daemon=True)
	else:
		urlthread=threading.Thread(target=ourthread,args=(None,webv,autoclosable,),daemon=True)
	urlthread.start()
	#box.set_parent(parent) if parent else False
	box.webv=webv
	box.goback=goback
	box.goforward=goforward
	box.reload=webv.reload
	return box
def openWebPage(page=None,traditional=False,name="Baggins",version="2.0",mainpage=None,private=False,kiosk=False,title=None,autoclosable=False,boxonly=False,search_engine="https://duckduckgo.com/?q=",aid=None,tabbed=False,vertabbed=True):
	def activate(application):
		window=Gtk.ApplicationWindow()
		window.set_application(application)
		box=openWebPage2(page=page,traditional=traditional,name=name,version=version,mainpage=mainpage,private=private,kiosk=kiosk,autoclosable=autoclosable,search_engine=search_engine,aid=aid)
		if not kiosk:
			tabbed=True
		if (tabbed):
			nb=Gtk.Notebook()
			nb.new()
			nb.set_show_tabs(False)
			def setshowtabs(nb):
				if (nb.get_n_pages()==1):
					nb.set_show_tabs(False)
				else:
					nb.set_show_tabs(True)
			def newtab(x):
				#GLib.idle_add(lambda: nb.append_page(openWebPage2(page=page, traditional=traditional, name=name, version=version, mainpage=mainpage, private=private, kiosk=kiosk, autoclosable=autoclosable, search_engine=search_engine, aid=aid,parent=nb)))
				box=openWebPage2(page="about:home", traditional=traditional, name=name, version=version, mainpage=mainpage, private=private, kiosk=kiosk, autoclosable=autoclosable, search_engine=search_engine, aid=aid,parent=nb)
				nb.append_page(box)
				nb.show()
				nb.set_current_page(-1)
				tab=nb.get_nth_page(-1)
				#nb.hide()
				nb.set_tab_reorderable(tab,True)
				nb.set_show_border(False)
				setshowtabs(nb)
				#nb.set_tab_label(tab,Gtk.Label(label=box.title))
			nb.append_page(box)
			if (vertabbed):
				nb.set_tab_pos(Gtk.PositionType.LEFT)
			window.set_child(nb)
			b=Gtk.Button.new_from_icon_name("tab-new")
			b.connect("clicked",newtab)
			b2=Gtk.Button.new_from_icon_name("application-exit-symbolic")
			#ag=Gtk.AccelGroup.new()
			#ag.connect(Gdk.keyval_from_name("t"),Gdk.ModifierType.CONTROL_MASK,Gtk.AccelFlags.VISIBLE,lambda a,b,c,d: newtab(1))
			def closetab(x):
				nb.remove_page(nb.get_current_page())
				setshowtabs(nb)
			def switchtab(forth):
					if (forth=="forth"):
						nb.next_page()
					else:
						nb.prev_page()
			#ag.connect(Gdk.keyval_from_name("w"),Gdk.ModifierType.CONTROL_MASK,Gtk.AccelFlags.VISIBLE,lambda a,b,c,d: closetab(1))
			#ag.connect(Gdk.keyval_from_name("b"),Gdk.ModifierType.CONTROL_MASK,Gtk.AccelFlags.VISIBLE,lambda a,b,c,d: switchtab("forth"))
			#ag.connect(Gdk.keyval_from_name("h"),Gdk.ModifierType.CONTROL_MASK,Gtk.AccelFlags.VISIBLE,lambda a,b,c,d: switchtab(False))
			cpage=nb.get_nth_page(nb.get_current_page())
			#ag.connect(Gdk.keyval_from_name("F5"),Gdk.ModifierType.CONTROL_MASK,Gtk.AccelFlags.VISIBLE,lambda a,b,c,d: cpage.reload())
			#ag.connect(Gdk.keyval_from_name("Left"),Gdk.ModifierType.MOD1_MASK,Gtk.AccelFlags.VISIBLE,lambda a,b,c,d: cpage.goback(cpage.webv))
			#ag.connect(Gdk.keyval_from_name("Right"),Gdk.ModifierType.MOD1_MASK,Gtk.AccelFlags.VISIBLE,lambda a,b,c,d: cpage.goforward(cpage.webv))
			b2.connect("clicked",closetab)
			hb=Gtk.HeaderBar()
			#hb.set_show_close_button(True)
			hb.pack_start(b)
			hb.pack_start(b2)
			window.set_titlebar(hb)
		else:
			window.set_child(box)
		window.set_default_size(1000,1000)
#		GLib.set_prgname(aid or "org.freedesktop.Baggins")
		window.set_title(title or "Baggins 2.1 “Balin Fundin’s son”")
#		window.add_accel_group(ag)
		window.present()
	application=Gtk.Application(application_id=aid)
	application.connect("activate",activate)
	application.run(None)
