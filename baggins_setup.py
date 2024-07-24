#!/usr/bin/env python3
import os
import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk
path="/".join(os.path.realpath(__file__).split("/")[:-1])
def saveetc(entry):
	global path
	text=entry.get_text()
	file=open(path+"/searchengine","w")
	file.write(text)
	file.close()
	Gtk.main_quit()
window=Gtk.Window()
window.connect("destroy",Gtk.main_quit)
window.set_title("Setup")
box=Gtk.Box()
window.add(box)
label=Gtk.Label(label="The search engine:")
box.pack_start(label,expand=False,fill=False,padding=0)
entry=Gtk.Entry()
entry.set_text(open(path+"/searchengine").read())
box.pack_start(entry,expand=False,fill=False,padding=0)
button=Gtk.Button(label="Save and exit")
button.connect("clicked",lambda x: saveetc(entry))
box.pack_start(button,expand=False,fill=False,padding=0)
window.show_all()
Gtk.main()
