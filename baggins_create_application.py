import os
import random
import gi
import urllib.parse
import urllib.request
gi.require_version("Gtk","3.0")
from gi.repository import Gtk
path=os.path.expanduser("~")+"/.local/share/applications/"
bagpath=os.path.expanduser("~")+"/.baggins"
def createApplication(urie,namee):
	global path
	uri=urie.get_text()
	name=namee.get_text()
	pars=urllib.parse.urlparse(uri)
	favicon=pars.scheme+"://"+pars.netloc+"/favicon.ico"
	num=str(random.randrange(1000000))
	try:
		favcontent=urllib.request.urlopen(favicon).read()
		iconpath=bagpath+"/baggins-"+num
		iconf=open(iconpath,"bw")
		iconf.write(favcontent)
		iconf.close()
	except:
		iconpath="web-browser"
	f=open(path+"org.freedesktop.Baggins"+num+".desktop","w")
	f.write("""
[Desktop Entry]
Name="""+name+"""
Type=Application
Icon="""+iconpath+"""
Exec=baggins -k --title " """+name+""" " " """+uri+""" " --aid """+"org.freedesktop.Baggins"+num+"""
Actions=Remove;

[Desktop Action Remove]
Exec=rm """+path+"org.freedesktop.Baggins"+num+".desktop """+iconpath+"""
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
