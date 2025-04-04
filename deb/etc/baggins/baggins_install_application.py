import sys
from baggins_create_application_lib import *
try:
	f=open(sys.argv[1])
except:
	print("Error")
	exit(1)
csv=f.read()
csv=csv.split("\n")
for i in range(len(csv)):
	csv[i]=csv[i].split("	")
try:
	appname=csv[1][1]
	uri=csv[2][1]
	createApplication(uri,appname,"")
except:
	print("Error")
