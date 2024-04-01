import sys
import urllib.request
import webview.menu as wm
import os
import time
import tkinter as tk
#locale probe
if (not os.path.exists("./locales")):
	print ("Localisation file does not exist, downloading...")
	try:
		if (os.path.exists("./get.conf")):
			getconf=open("get.conf")
			getconfcontent=getconf.read()
			getconf.close()
			getconfcontent=getconfcontent.split("\n")
			ourContent=urllib.request.urlopen(getconfcontent[3]).read().decode()				
		else:
			ourContent=urllib.request.urlopen("https://zalan.withssl.com/en/baggins/locales_en_1.0")
	except Exception as ourex:
		print ("Failed, exiting.")
		print (ourex)
		exit (1)
	else:
		localesf=open("./locales","w")
		localesf.write(ourContent)
		localesf.close()
locales=open("./locales")
localesc=locales.read()
locales.close()
localesc=localesc.replace("\n","")
localesc=localesc.split("SEPARATOR")
#support probe
leftsecs=1727924399-time.time()
if (leftsecs > 0 and leftsecs<=864000):
	print ("The support of your version will end in "+str(leftsecs)+" seconds, what is equivalent by " + str(leftsecs/86400) + " days. Please, consider upgrading to a newer one.")
	window=tk.Tk()
	window.title("The end of support is near")
	labelle=tk.Label(window,text="The support of your version will end in  "+str(leftsecs)+" seconds, what is equivalent by "+str(leftsecs/86400)+" days. Please, consider upgrading to a newer one. Close this window to proceed.")
	labelle.pack()
	window.mainloop()
if (time.time()>1727924399): # October 3 2024, 04:59:59 GMT
	print ("Your current Baggins version is not supported, please, upgrade to a newer one. You can run Baggins with -U and then -u to do this.")
	window=tk.Tk()
	window.title("The support ended")
	tk.Label(window,text="Your current Baggins version is not supported, please, upgrade to a newer one. You can run Baggins with -U and then -u to do this.").pack()
	window.mainloop()
	if (time.time()>1735703999): # January 1 2025, 04:59:59 GMT
		if (not os.path.exists("IWillUpgradeIPromise")):
			print ("Your version is extremely old, create  IWillUpgradeIPromise to run Baggins.")
			window=tk.Tk()
			window.title("Extremely old version")
			tk.Label(window,text="Your version is extremely old, create file IWillUpgradeIPromise to run Baggins.").pack()
			window.mainloop()
			exit (1)
#Function
def getgetconf():
	global localesc
	ourFile=open("./get.conf","w")
	try:
		thisContent=urllib.request.urlopen(open("getget.conf.conf").read()).read().decode()
	except Exception as MyException:
		print (localesc[0]+str(MyException))# print error message
		ourFile.close()
	else:
		if (thisContent!=""):
			ourFile.write(thisContent)
			ourFile.close()
			print (localesc[1])
		else:
			print ("")
#get.conf probe
if (not os.path.exists("./get.conf")):
	print (localesc[2]) # print information message
	getgetconf()
try:
	import webview
except:
	import subprocess
	try:
		subprocess.run("pip install webview",shell=True)
		print (localesc[3])#webview is installed, you need to run Baggins again
		exit(0)
	except:
		print (localesc[4]) # print error message about EME
		exit (0)
webview.settings = {
  'ALLOW_DOWNLOADS': True,
  'ALLOW_FILE_URLS': True,
  'OPEN_EXTERNAL_LINKS_IN_BROWSER': False,
  'OPEN_DEVTOOLS_IN_DEBUG': True
}
getconfcontent=open("./get.conf")
getconfcontent2=getconfcontent.read()
getconfcontent.close()
getconfcontent=getconfcontent2
getconfcontent=getconfcontent.split("\n")
if (len(sys.argv)==2):
	if (sys.argv[1]=="-o" or sys.argv[1]=="--online"):#online mode to remove
		def goBack():
			webview.active_window().load_url("./mainpage_Otho.html")
		webview.create_window(localesc[8],"./mainpage_Otho.html",text_select=True,zoomable=True) # localesc[8] is the title
		itemsOfMenu=[wm.Menu(localesc[9],[wm.MenuAction(localesc[10],goBack)])]
		webview.start(storage_path="./pywebview/",private_mode=False,menu=itemsOfMenu)
	elif (sys.argv[1]=="-h" or sys.argv[1]=="--help"):
		print (localesc[5])
	elif (sys.argv[1]=="-u" or sys.argv[1]=="--update"):
		print (localesc[6])
		try:
			pyscriptcontent=urllib.request.urlopen(getconfcontent[0]).read().decode()
		except Exception as myException:
			print ("Failed to update Baggins. Check your internet connection and the availability of zalan.withssl.com. The error message:")
			print (str(myException))
		else:
			if (pyscriptcontent==""):
				print ("Something went wrong.")
			else:
				pyscriptfile=open(sys.argv[0],"w")
				pyscriptfile.write(pyscriptcontent)
				pyscriptfile.close()
				print (localesc[7])
	elif (sys.argv[1]=="-U" or sys.argv[1]=="--full-upgrade"):
		getgetconf()
		getconfcontent=open("./get.conf")
		getconfcontent2=getconfcontent.read()
		getconfcontent.close()
		getconfcontent=getconfcontent2
		getconfcontent=getconfcontent.split("\n")
		bilbopng=urllib.request.urlopen(getconfcontent[1]).read()
		bilbopng_file=open("Bilbo.png","bw")
		bilbopng_file.write(bilbopng)
		bilbopng_file.close()
		mainpage=urllib.request.urlopen(getconfcontent[2]).read()
		mainpage_local=open("./mainpage_Otho.html","bw")
		mainpage_local.write(mainpage)
		mainpage_local.close()
		locales=urllib.request.urlopen(getconfcontent[3]).read().decode()
		locales_local=open("locales","w")
		locales_local.write(locales)
		locales_local.close()
	elif (sys.argv[1]=="-p" or sys.argv[1]=="--private"):
		webview.create_window(localesc[8],"./mainpage_Otho.html",text_select=True,zoomable=True)
		itemsOfMenu=[wm.Menu(localesc[9],[wm.MenuAction(localesc[10],goBack)])]
		webview.start(private_mode=True,menu=itemsOfMenu)
	elif (sys.argv[1]=="--none" or sys.argv[1]=="-0"):
		exit(0)
	else:
		webview.create_window(localesc[8],sys.argv[1],text_select=True,zoomable=True)
		itemsOfMenu=[wm.Menu(localesc[9],[wm.MenuAction(localesc[10],goBack)])]
		webview.start(storage_path="./pywebview/",private_mode=False,menu=itemsOfMenu)
else:
	def setValue(entrie,text):
		entrie.delete(0,tk.END)
		entrie.insert(0,text)
	def openSite(entrie):
		retrievedValue=entrie.get()
		webview.active_window().load_url(retrievedValue)
	def urlEnter():
		window=tk.Tk()
		window.title(localesc[11])
		window.protocol("WM_DELETE_WINDOW", lambda: True)
		def properClose(window):
			try:
				webview.active_window().destroy()
			except:
				window.destroy()
				exit(0)
			window.destroy()
			exit(0)
		entrie=tk.Entry(window)
		entrie.grid(row=0,column=0)
		loadURLButton=tk.Button(text=localesc[12],command=lambda entrie=entrie: openSite(entrie))
		loadURLButton.grid(row=0,column=1)
		updateURLButton=tk.Button(text=localesc[13],command=lambda: setValue(entrie,webview.active_window().get_current_url()))
		updateURLButton.grid(row=1,column=0)
		properQuitButton=tk.Button(text=localesc[14],command=lambda: properClose(window))
		properQuitButton.grid(row=1,column=1)
		window.mainloop()
	webview.create_window(localesc[8],"./mainpage_Otho.html",text_select=True,zoomable=True)
	webview.start(func=urlEnter,storage_path="./pywebview",private_mode=False)
