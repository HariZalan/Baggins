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
def openWebPage(page=None,traditional=False,name="Baggins",version="2.2",mainpage=None,private=False,kiosk=False,title=None,autoclosable=False,boxonly=False,search_engine="https://duckduckgo.com/?q=",aid=None,tabbed=False,vertabbed=True,applicationn=None):
	if (applicationn==None):
		application=Gtk.Application(application_id=aid or "org.freedesktop.Baggins",flags=Gio.ApplicationFlags.ALLOW_REPLACEMENT)
	else:
		application=applicationn
	def activate(application,tabbed=False):
		window=Gtk.ApplicationWindow()
		window.set_application(application)
		box=openWebPage2(page=page,traditional=traditional,name=name,version=version,mainpage=mainpage,private=private,kiosk=kiosk,autoclosable=autoclosable,search_engine=search_engine,aid=aid,application=application)
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
				box=openWebPage2(page="about:home", traditional=traditional, name=name, version=version, mainpage=mainpage, private=private, kiosk=kiosk, autoclosable=autoclosable, search_engine=search_engine, aid=aid,parent=nb)
				box.set_focusable(False)
				nb.append_page(box)
				nb.show()
				nb.set_current_page(-1)
				tab=nb.get_nth_page(-1)
				nb.set_tab_reorderable(tab,True)
				nb.set_show_border(False)
				setshowtabs(nb)
			nb.append_page(box)
			if (vertabbed):
				nb.set_tab_pos(Gtk.PositionType.LEFT)
			window.set_child(nb)
			window.set_focus(nb)
			window.set_focus_on_click(False)
			b=Gtk.Button.new_from_icon_name("tab-new")
			b.connect("clicked",newtab)
			b2=Gtk.Button.new_from_icon_name("application-exit-symbolic")
			cpage=nb.get_nth_page(nb.get_current_page())
			def webvkeypress(controller,keyval,keycode,state,ctrl):
				ctrl.emit("key-pressed",keyval,keycode,state)
				return False
			def keypress(keyval,state,nb):
				if state and Gdk.ModifierType.CONTROL_MASK:
					if keyval==Gdk.KEY_t:
						newtab(1)
					elif keyval==Gdk.KEY_w:
						closetab(1)
					elif keyval==Gdk.KEY_b:
						switchtab("forth")
					elif keyval==Gdk.KEY_h:
						switchtab(False)
					elif keyval==Gdk.KEY_F5:
						cpage.reload()
				elif state and Gdk.ModifierType.ALT_MASK:
					if keyval==Gdk.KEY_Left:
						cpage.goback(cpage.webv)
					elif keyval==Gdk.KEY_Right:
						cpage.goforward(cpage.webv)
				return False
			ctrl=Gtk.EventControllerKey()
			ctrl.connect("key-pressed",lambda controller, keyval, keycode, state: keypress(keyval, state, nb))
			window.add_controller(ctrl)
			ctrl2=Gtk.EventControllerKey()
			cpage.webv.add_controller(ctrl2)
			ctrl2.connect("key-pressed",lambda controller,keyval,keycode, state: webvkeypress(controller,keyval,keycode,state,ctrl))
			def closetab(x):
				nb.remove_page(nb.get_current_page())
				setshowtabs(nb)
			def switchtab(forth):
					if (forth=="forth"):
						nb.next_page()
					else:
						nb.prev_page()
			b2.connect("clicked",closetab)
			hb=Gtk.HeaderBar()
			hb.pack_start(b)
			hb.pack_start(b2)
			window.set_titlebar(hb)
		else:
			window.set_child(box)
		window.set_default_size(1000,1000)
		window.set_title(title or "Baggins 2.2 “Thorin Oakshield”")
		window.present()
	if (applicationn==None):
		application.connect("activate",activate)
		application.run(None)
	else:
		activate(application, tabbed)
def openWebPage2(page=None,traditional=False,webv=None,name="Baggins",version="2.2",mainpage=None,private=False,kiosk=False,title=None,autoclosable=False,boxonly=False,search_engine="https://duckduckgo.com/?q=",aid="org.freedesktop.Baggins",parent=None,application=None,webvkeypress=None):
	if (aid==None):
		aid="org.freedesktop.Baggins"
	if (kiosk==True):
		traditional=True
	import threading
	if (page=="about:home" or page==None):
		page=mainpage
	try:
		provider=Gtk.CssProvider()
		provider.load_from_file(Gio.File.new_for_path(bagpath+"/ui.css"))
		Gtk.StyleContext.add_provider_for_display(Gdk.Display.get_default(),provider,Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)
	except Exception as e:
		print ("Failed to load CSS, the browser will work, but the GUI shall be poor. The exception:")
		print (e)
	if (kiosk==False):
		def searchorgo(entry,webv):
			if (entry.get_text()!="about:home"):
				url=entry.get_text()
				paersar=urllib.parse.urlparse(url)
				if (paersar.scheme):
					webv.load_uri(url)
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
					GLib.idle_add(lambda: reload.set_sensitive(False))
				else:
					GLib.idle_add(lambda: reload.set_sensitive(True))
	def displayuri(attercop,hittestresult,oldtomnoddy,TheThirdOne,traditional):
		if (hittestresult.context_is_link()==True):
			TheThirdOne.set_visible(True)
			TheThirdOne.set_text(WebKit2.uri_for_display(hittestresult.get_link_uri()))
		else:
			TheThirdOne.set_text("")
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
	icon=bilbospath+"/Bilbo.png"
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
			dialogue=Gtk.Window()
			label=Gtk.Label(label="A download has started.")
			box=Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
			dialogue.set_child(box)
			box.append(label)
			ok=Gtk.Button(label="I have acknowledged")
			ok.connect("clicked",lambda x: dialogue.destroy())
			box.append(ok)
			dialogue.present()
		def downstart(session,download):
			download.connect("decide-destination",decdest)
		WebKit2.NetworkSession.get_default().connect("download-started",downstart)
		WebKit2.NetworkSession.get_default().set_itp_enabled(True)
		webv.connect("create",lambda x,y: openinnewwindow(x,y,kiosk,traditional,private,title,application))
		webv.connect("mouse-target-changed",lambda x,y,z: displayuri(x,y,z,The_third_one,traditional))
		webv.connect("load-failed-with-tls-errors",loadfailed)
		if (private==False):
			webv.cookieManager=WebKit2.NetworkSession.get_default().get_cookie_manager()
			WebKit2.CookieManager.set_persistent_storage(webv.cookieManager,bagpath+"/.baggins.storage",WebKit2.CookiePersistentStorage(WebKit2.CookiePersistentStorage.TEXT))
		settings=webv.get_settings()
		WebKit2.Settings.set_user_agent_with_application_details(settings,name,version)
		webv.load_uri(page)
		WebKit2.Settings.set_enable_webrtc(settings,True)
		WebKit2.Settings.set_enable_media_stream(settings,True)
		WebKit2.Settings.set_enable_developer_extras(settings,True)
		WebKit2.Settings.set_enable_back_forward_navigation_gestures(settings,True)
		WebKit2.Settings.set_default_charset(settings,"utf-8")
		WebKit2.Settings.set_javascript_can_access_clipboard(settings,True)
		def aboutdialog():
			import about
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
		def cameraandmicrophone(application,b):
			if 1:
				window=Gtk.Window()
				box=Gtk.Box()
				window.set_child(box)
				label=Gtk.Label.new("The site wants to request a permission.")
				button1=Gtk.Button(label="Permit")
				button2=Gtk.Button(label="Deny")
				button1.connect("clicked", lambda x: permit())
				button2.connect("clicked", lambda x: deny())
				box.append(label)
				box.append(button1)
				box.append(button2)
				window.set_application(application)
				window.present()
				result=False
				def permit():
					window.destroy()
					b.allow()
				def deny():
					window.destroy()
					nonlocal result
					result=True
					b.deny()
					
				return result
		webv.connect("permission-request", lambda x,y: cameraandmicrophone(application,y))
		webv.connect("web-process-terminated",lambda x,y: terminated(x))
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
		button7=Gtk.Button.new_from_icon_name("help-about-symbolic")
		button7.connect("clicked",lambda x: aboutdialog())
		#button7=Gtk.Button.new_from_icon_name("application-x-addon-symbolic")
		box2.append(button)
		box2.append(button2)
		box2.append(button5)
		box2.append(entrie)
		box2.append(button0)
		box2.append(button4)
		box2.append(button6)
		box2.append(button7)
	box=Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
	The_third_one=Gtk.Label()
	if (traditional==True):
		box.append(webv)
		if (kiosk==False):
			box.prepend(box2)
		box.prepend(The_third_one)
	else:
		box.prepend(The_third_one)
		if (kiosk==False):
			box.append(box2)
		webvbox=Gtk.Box()
		webvbox.prepend(webv)
		box.prepend(webvbox)
	if(box!=None):
		box.title=webv.get_title()
	if (kiosk==False):
		urlthread=threading.Thread(target=ourthread,args=(entrie,webv,autoclosable,button,button2,button5,box,),daemon=True)
	else:
		urlthread=threading.Thread(target=ourthread,args=(None,webv,autoclosable,),daemon=True)
	urlthread.start()
	webv.set_focusable(False)
	box.webv=webv
	box.goback=goback
	box.goforward=goforward
	box.reload=webv.reload
	return box
def openinnewwindow(wv,navact,kiosk,traditional,private,title,application):
	x=navact.get_request().get_uri()
	openWebPage(page=x,kiosk=kiosk,traditional=traditional,private=private,title=title,applicationn=application)
	return None
