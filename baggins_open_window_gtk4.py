#!/usr/bin/env python3
import os
bilbospath=os.path.realpath(os.path.dirname(os.path.realpath(__file__)))
bagpath=os.path.expanduser("~")+"/.baggins"
import gi
gi.require_version("Gtk","4.0")
gi.require_version("WebKit","6.0")
from gi.repository import Gtk, Gdk, Gio, GLib
from gi.repository import WebKit as WebKit2
from baggins_create_webview_et_al import *
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
				box=openWebPage2(page="about:home", traditional=traditional, name=name, version=version, mainpage=mainpage, private=private, kiosk=kiosk, autoclosable=autoclosable, search_engine=search_engine, aid=aid,parent=nb)
				box.set_focusable(False)
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
			window.set_focus(nb)
			window.set_focus_on_click(False)
			b=Gtk.Button.new_from_icon_name("tab-new")
			b.connect("clicked",newtab)
			b2=Gtk.Button.new_from_icon_name("application-exit-symbolic")
			cpage=nb.get_nth_page(nb.get_current_page())
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
			ctrl2.connect("key-pressed",lambda controller, keyval, keycode, state: False)
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
			#hb.set_show_close_button(True)
			hb.pack_start(b)
			hb.pack_start(b2)
			window.set_titlebar(hb)
		else:
			window.set_child(box)
		window.set_default_size(1000,1000)
		window.set_title(title or "Baggins 2.2 “Thorin Oakshield”")
		window.present()
	application=Gtk.Application(application_id=aid or "org.freedesktop.Baggins")
	application.connect("activate",activate)
	application.run(None)
