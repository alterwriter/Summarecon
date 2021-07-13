from shutil import *
from subprocess import *

#Wappalyzer INSTALLATION

#installation
def toolInstall():
	install=print("choose the type of User Interface to install wapplazer :\n[1] CLI WIndows\n[2] CLI Ubuntu")
	takeInput=input(":")
	
	if takeInput == "1":
		print(call("pip install --upgrade python-Wappalyzer", shell=True))

	elif takeInput == "2":
		print(call("npm i -g wappalyzer", shell=True))
	
def toolScan():
	check1=which("Wappalyzer")
	check2=which("wappalyzer")
	test=print(check1, check2)

	if check1=="C:/Python38-32/Lib/site-packages/Wappalyzer":
		print("[*] Wappalyzer siap digunakan")

	if check2=="/usr/bin/wappalyzer":
		print("[*] Wappalyzer siap digunakan")

	elif "none":
		print("[*] please install Wappalyzer")
		print()
		toolInstall()

toolScan()
