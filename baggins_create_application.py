import os
import random
import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk
path=os.path.expanduser("~")+"/.local/share/applications/"
def createApplication(urie,namee):
	global path
	uri=urie.get_text()
	name=namee.get_text()
	num=random.randrange(1000000)
	f=open(path+"baggins-"+str(num)+".desktop","w")
	f.write("""
[Desktop Entry]
Name="""+name+"""
Type=Application
Icon=web-browser
Exec=baggins -k --title " """+name+""" " " """+uri+""" "
Actions=Remove;

[Desktop Action Remove]
Exec=rm """+path+"baggins-"+str(num)+".desktop"+"""
Name=Remove
""")
	f.close()
	Gtk.main_quit()
window=Gtk.Window()
window.connect("destroy",Gtk.main_quit)
window.set_title("Create web application")
box=Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
entry=Gtk.Entry()
entry.set_placeholder_text("The URI")
entry2=Gtk.Entry()
entry2.set_placeholder_text("The name of the application")
button=Gtk.Button(label="Create")
button.connect("clicked",lambda x: createApplication(entry,entry2))
box.pack_start(entry,fill=False,expand=False,padding=1)
box.pack_start(entry2,fill=False,expand=False,padding=1)
box.pack_start(button,fill=False,expand=False,padding=1)
window.add(box)
window.show_all()
Gtk.main()
