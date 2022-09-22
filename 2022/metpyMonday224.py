# Metpy Monday
# 224 - SFTP and paramiko
# https://www.youtube.com/watch?v=bkN3x3JknG0

# conda install -c conda-forge paramiko

import paramiko
from datetime import datetime

myhost = 'server123'
mypwd = 'abc123'
myuser = 'jane'

myport = 22

# Setup the transport object
with paramiko.Transport((myhost, myport)) as transport:
	transport.connect(None, myuser, mypwd)
	
	# Create SFTP client
	with paramiko.SFTPClient.from_transport(transport) as sftp:
	
		fname = f'map_{datetime.utcnow():%Y%m%d%H}.png'
	
		# Put the file
		sftp.put('temp.png', fname)	
	
		# List files
		print(stfp.listdir())
	
		# Get the file
		sftp.get(fname, fname)	
	
		# Remove the file
		sftp.remove(fname)	
	
		# List files
		print('*' * 80)
		print(sftp.listdir())
