#!/usr/bin/env python3
import os
import random
import gi
import urllib.parse
import urllib.request
gi.require_version("Gtk","4.0")
from gi.repository import Gtk
from baggins_create_application_lib import createApplication
path=os.path.expanduser("~")+"/.local/share/applications/"
bagpath=os.path.expanduser("~")+"/.baggins"
def activate(application):
	window=Gtk.ApplicationWindow()
	window.set_application(application)
	window.set_title("Create web application")
	box=Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
	entry=Gtk.Entry()
	entry.set_placeholder_text("The URI")
	entry2=Gtk.Entry()
	entry2.set_placeholder_text("The name of the application")
	button=Gtk.Button(label="Create")
	button.connect("clicked",lambda x: (createApplication(entry.get_text(),entry2.get_text(),window), window.destroy()))
	box.append(entry)
	box.append(entry2)
	box.append(button)
	window.set_child(box)
	window.present()
application=Gtk.Application()
application.connect("activate",activate)
application.run(None)
