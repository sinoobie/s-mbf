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
	os.system('clear')
	print(banner)
	print("[ex] https://www.facebook.com/100009256XXXXX/posts/223037817XXXXX/?app=fbl")
	tr=input("[?] target link: ").replace('https://www.facebook.com/','').replace('/posts/','_').replace('/?app=fbl','')
	print("\n[info] type '<n>' for newlines")
	msg=input("[?] comment: ")
	if msg == '':
		exit("[?] are you stupid")
	ms=msg.replace('<n>','\n')
	print("\n[recomended] 1-100")
	lo=int(input("[?] loop: "))
	print()
	co=int(1)
	toket=open('toket/token.txt','r').read()
	for i in range(lo):
		par = {'access_token' : toket, 'message' : ms}
		pt=requests.post('https://graph.facebook.com/'+tr+'/comments',data=par)
		post=json.loads(pt.text)
		if 'error' in str(post):
			print('['+str(co)+'] Err: an error occurred')
		else:
			print('['+str(co)+'] successfully comments')
		co+=1
	print("[^•^] done")
except Exception as F:
	exit("\n[Error] %s"%(F))
