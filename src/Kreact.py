#!usr/bin/python3.7
#Author: KANG-NEWBIE
#Contact: t.me/kang_nuubi
#github: github.com/kang-newbie
'''
recode? oke, but don't deleted name author
'''
try:
	import requests, sys, os, time, json

	banner=("""
\t\t[ Facebook Comments Reaction ]
\t\t     [ By : KANG-NEWBIE ]
""")
	tp=("""\n\t[react]
1. Like \t4.Wow
2. Love \t5.Sad
3. Haha \t6.Angry""")
	os.system('clear')
	print(banner)
	print("[ex] https://www.facebook.com/100009256XXXXX/posts/22303781XXXXX")
	link=input("[?] link target: ").replace('https://www.facebook.com/','').replace('/posts/','_')

	print(tp)
	pilih=int(input("/react_> "))
	if pilih == 1:
		react='LIKE'
	elif pilih == 2:
		react='LOVE'
	elif pilih == 3:
		react='HAHA'
	elif pilih == 4:
		react='WOW'
	elif pilih == 5:
		react='SAD'
	elif pilih == 6:
		react='ANGRY'
	else: exit("[?] are you stupid")

	toket=open('toket/token.txt','r').read()
	req=requests.get('https://graph.facebook.com/'+link+'/comments?access_token='+toket)
	j=json.loads(req.text)
	for i in j['data']:
		print("[get]",i['id']);sys.stdout.flush();time.sleep(0.1)

	print("[!] start.");time.sleep(3);os.system('clear')
	par={'access_token':toket,'type':react}
	for i in j['data']:
		url="https://graph.facebook.com/v3.2/"+i['id']+"/reactions"
		requs=requests.post(url,data=par)
		if 'success' in str(requs.text):
			print("[+] "+i['id']+" reacted")
		else: print("[!] something error")
	print("[^•^] done")
except Exception as F:
	exit("[Err] %s"%(F))
