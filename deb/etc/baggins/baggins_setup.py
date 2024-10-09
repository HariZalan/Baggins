#!/usr/bin/env python3
import os
import gi
gi.require_version("Gtk","4.0")
gi.require_version("Adw","1")
from gi.repository import Gtk, Adw
bagpath=os.path.expanduser("~")+"/.baggins"
if (not os.path.exists(bagpath)):
	os.mkdir(bagpath)
def saveetc(entry,window):
	global path
	text=entry.get_text()
	file=open(bagpath+"/searchengine","w")
	file.write(text)
	file.close()
	window.destroy()
def activate(application):
	window=Gtk.ApplicationWindow()
	window.set_application(application)
	window.set_title("Setup")
	box=Gtk.Box()
	window.set_child(box)
	label=Gtk.Label(label="The search engine:")
	box.append(label)
	entry=Gtk.Entry()
	entry.set_text(open(bagpath+"/searchengine").read())
	box.append(entry)
	button=Gtk.Button(label="Save and exit")
	button.connect("clicked",lambda x: saveetc(entry,window))
	box.append(button)
	window.present()
application=Gtk.Application(application_id="org.freedesktop.Baggins")
application.connect("activate",activate)
application.run(None)
