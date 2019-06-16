import mechanize,os
from multiprocessing.pool import ThreadPool

class Ubahpw:
	def __init__(self):
		self.u='https://mbasic.facebook.com{}'
		self.banner()

	def banner(self):
		print("""
	;;;;;;;;;;;;;;;;;;;;;;;
	; Auto Reset Password ;
	;   By KANG-NEWBIE    ;
	;;;;;;;;;;;;;;;;;;;;;;;
	""")
		self.kun()

	def kun(self):
		print('[!] sparator email|password')
		try:
			fil=input('[?] List Accounts: ')
			self.file=open(fil,'r').read().splitlines()
		except FileNotFoundError:
			exit('[!] File Not Found')
		print('[!] Password must be 6 characters or more')
		self.pbaru=input('[?] New Password: ')
		for i in self.file:
			self.login(i)
		print('[done] file save as: result/newpass.txt')
	def login(self,ids):
		try:
			global br
			br = mechanize.Browser()
			br.set_handle_equiv(True)
			br.set_handle_gzip(True)
			br.set_handle_redirect(True)
			br.set_handle_referer(True)
			br.set_handle_robots(False)
			br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
			br.addheaders = [('User-Agent','Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.114 Mobile Safari/537.36')]
			br.open(self.u.format('/login'))
			br.select_form(nr=0)
			br.form['email']=ids.split('|')[0]
			br.form['pass']=ids.split('|')[1]
			sub=br.submit().read()
			if 'save-device' in str(sub) or 'm_sess' in str(sub):
				self.ganti(ids)
			else:
				print(f'[Failed] {ids}')
		except a: pass

	def ganti(self,ids):
		br.open(self.u.format('/settings/security/password/'))
		br._factory.is_html = True
		br.select_form(nr=1)
		br.form['password_old']=ids.split('|')[1]
		br.form['password_new']=self.pbaru
		br.form['password_confirm']=self.pbaru
		mit=br.submit().read()
		if 'Kata Sandi Telah Diubah' in str(mit) or 'Password Changed' in str(mit):
			try:
				os.mkdir('result')
			except: pass
			pc=open('result/newpass.txt','a')
			pc.write(f"{ids.split('|')[0]}|{self.pbaru}\n")
			print(f"[success] {ids} >> {ids.split('|')[0]}|{self.pbaru}")

Ubahpw()