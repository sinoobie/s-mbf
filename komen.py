#!usr/bin/python3.7
#Author: KANG-NEWBIE
#Github: https://github.com/kang-newbie
#Contact: t.me/kang_nuubi
'''
boleh recode asal cantumkan author aslinya goblok!
'''
try:
	import requests
	from multiprocessing.pool import ThreadPool
	import os, sys, json, time, hashlib

	banner=("""
 _                              _         
| |        F A C E B O O K     | |        
| | _____  _ __ ___   ___ _ __ | |__ _ _  
| |/ / _ \| '_ ` _ \ / _ \ '_ \| __/ _` | 
|   < (_) | | | | | |  __/ | | | || (_| | 
|_|\_\___/|_| |_| |_|\___|_| |_|\__\__,_| 
                                         """)
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
			requ=requests.get('https://api.facebook.com/restserver.php',params=data)
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
	os.system('clear')
	print(banner)
	print("[info] ketik '<n>' untuk garis baru")
	msg=input("[?] comment: ")
	if msg == '':
		exit("[!] tulis komennya goblok")
	ms=msg.replace('<n>','\n')
	def main(arg):
		global ms,toket
		par = {'access_token' : toket, 'message' : ms}
		pt=requests.post('https://graph.facebook.com/'+arg+'/comments',data=par)
		post=json.loads(pt.text)
		print('[+] ['+arg+'] commented')

	id=[]
	toket=open('toket/token.txt','r').read()
	req = requests.get('https://graph.facebook.com/v3.0/me?fields=home.limit(100)&access_token='+toket)
	result = json.loads(req.text)
	for i in result['home']['data']:
		id.append(i['id'])
		print('\r[id] %s retrieved '%(i['id'])),;sys.stdout.flush();time.sleep(0.1)
	print("[!] Start.")
	time.sleep(2)
	os.system('clear')
	T=ThreadPool(10)
	T.map(main,id)
	print("[^•^] done")
except Exception as F:
	exit("\n[Error] %s"%(F))
