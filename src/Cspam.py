#!usr/bin/python3.7
#Author: KANG-NEWBIE
#contact: t.me/kang_nuubi
#thanks to all member CRABS_ID (t.me/CRABS_ID)

'''
recode? ok, but don't delete the author name
'''
try:
	import requests,mechanize,json,os,sys,time

	def login(usr,pws):
		global br,res
		br=mechanize.Browser()
		br.set_handle_robots( False )
		br.set_handle_refresh( mechanize._http.HTTPRefreshProcessor(), max_time = 1 )
		br.addheaders = [ ( 'User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1' ) ]
		br.open('https://mbasic.facebook.com/login')
		br.select_form(nr=0)
		br.form["email"] = usr
		br.form["pass"] = pws
		res=br.submit().read()

	def send(id,msg,lop):
		if 'save-device' in str(res) or 'm_sess' in str(res):
			for i in range(int(lop)):
				print("[+] sending messages to "+id)
				br.open('https://mbasic.facebook.com/messages/thread/'+id+'/')
				br.form = list(br.forms())[1]
				control = br.form.find_control("body")
				for control in br.form.controls:
					if control.type == "submit":
						control.disabled = True
				br["body"]=msg
				br.submit()
		else: exit("[!] login failed")

	def getid(msg,limit):
		ket=open('toket/token.txt','r').read()
		re=requests.get('https://graph.facebook.com/me/?fields=friends.limit('+limit+')&access_token='+ket).text
		js=json.loads(re)
		for i in js['friends']['data']:
			send(i['id'],msg,1)
#			print(i['id'])

	os.system('clear')
	print("""
	[ Facebook chat spammer ]
	   [ By:KANG-NEWBIE ]

1. Target chat spammer
2. Mass chat spammer
""")
	pil = int(input("/kang-newbie_> "))
	if pil == 1:
		usr=input("\n[?] username: ")
		pws=input("[?] password: ")
		print("\n[Info] type '<n>' for newlines")
		msg=input("[?] message : ").replace('<n>','\n')
		id=input("[?] target id: ")
		lop=input("[?] looping : ")
		print()
		login(usr,pws)
		send(id,msg,lop)
	elif pil == 2:
		usr=input("\n[?] username: ")
		pws=input("[?] password: ")
		print("\n[Info] type '<n>' for newlines")
		msg=input("[?] message : ").replace('<n>','\n')
		limit=input("[?] how many: ")
		login(usr,pws)
		getid(msg,limit)

except KeyboardInterrupt:
	exit("[Exit] key interrupt")
except Exception as F:
	print("Err: %s"%(F))