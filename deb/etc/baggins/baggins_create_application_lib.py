import urllib.parse
import urllib.request
import random
import os
path=os.path.expanduser("~")+"/.local/share/applications/"
bagpath=os.path.expanduser("~")+"/.baggins"
def createApplication(urie,namee,window):
	global path
	uri=urie
	name=namee
	pars=urllib.parse.urlparse(uri)
	favicon="https://icons.duckduckgo.com/ip2/"+pars.netloc+".ico"
	print(favicon)
	num=str(random.randrange(1000000))
	try:
		favcontent=urllib.request.urlopen(favicon).read()
		iconpath=bagpath+"/baggins-"+num
		iconf=open(iconpath,"bw")
		iconf.write(favcontent)
		iconf.close()
	except Exception as e:
		iconpath="web-browser"
		print(e)
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
	#window.destroy()
