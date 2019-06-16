import os

try:
	os.mkdir('../s-mbf_backupdir')
except: pass
try:
	os.system('mv result ../s-mbf_backupdir')
	print('[moving] result folder')
except: pass
try:
	os.system('mv checker ../s-mbf_backupdir')
	print('[moving] checker folder')
except: pass
try:
	os.system('mv toket ../s-mbf_backupdir')
	print('[moving] toket folder')
except: pass