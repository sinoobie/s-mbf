import requests,time,os
from http.cookiejar import LWPCookieJar as kuki
from getpass import getpass

def cek():
	try:
		s.cookies=kuki('toket/kue.txt')
		s.cookies.load()
		cek=s.get('https://mbasic.facebook.com/me').text
		if 'mbasic_logout_button' in cek:
			print('[√] cookies valids\n')
			a='True'
			return a
		else:
			print('[!] cookies invalid')
			os.remove('toket/kue.txt')
			a='False'
			return a
	except:
		print('[!] cookies invalid')
		os.remove('toket/kue.txt')
		a='False'
		return a

def login(self):
	global s
	print("\n[!] checking cookies")
	time.sleep(1)
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
		res = s.post('https://mbasic.facebook.com/login',data=data).text
		if 'm_sess' in str(res) or 'save-device' in str(res):
			s.cookies.save()
		else:
			exit('[!] fail login into your account')
	if 'True' in cek():
		pass
	else:
		exit()