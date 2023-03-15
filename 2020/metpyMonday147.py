# Metpy Monday
# 147 - Making the GFS Text You with Twilio Part 1
# https://www.youtube.com/watch?v=yPl_3e1f3sQ

# conda install -c conda-forge twilio

from twilio.rest import Client

# See twil.io/secure
account_sid = ''
auth_token = ''

from_number = ''
to_number = ''

# Replace this with data
max_temp = 95
min_temp = 73

client = Client(account_sid, auth_token)

message_text = f'24 hr GFS Max T: {max_temp} degF Min T: {min_temp} degF'

if min_temp <= 32:
	message_text += 'FREEZE HAZARD'
	
message = client.messages.create(body = message_text, from = from_number, to = to_number)

print(message.sid)
