# Metpy Monday
# 223 - Uploading to an FTP server from Python
# https://www.youtube.com/watch?v=Viy7wlRUpwA

myhost = 'server123'
mypwd = 'abc123'
myuser = 'jane'

from ftplib import FTP

with FTP(myhost, user = myuser, passwd = mypwd) as ftp:
	ftp.dir()
	# upload
	with open('temp.png', 'rb') as f:
		ftp.storbinary('STOR temp.png', f)
	print('*' * 80)
	ftp.dir()
	# rename
	ftp.rename('temp.png', 'myplot.png')
	print('*' * 80)
	ftp.dir()
	

with FTP(myhost, user = myuser, passwd = mypwd) as ftp:
	with open('archived_plot.png', 'wb') as f:
		ftp.retrbinary('RETR myplot.png', f.write)
	ftp.dir()
	print('*' * 80)
	# delete
	ftp.delete('myplot.png')
	ftp.dir()
