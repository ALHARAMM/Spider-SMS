from twilio.rest import Client
from colorama import Fore
import time

time.sleep(0.2)
print(Fore.LIGHTGREEN_EX+'''
(`  . | _   (`|\/|(`
_)|)|(|(/_|`_)|  |_)
  |
1.5
By ALHARAM

      ''')
# Your Twilio account credentials
account_sid = 'Your Sid'
auth_token = 'Your Token'

# Create a Twilio client
client = Client(account_sid, auth_token)

# Send a message
message = client.messages.create(
    body='Write Your Message Here',
    from_='Your Number',
    to='The Victim Number'
    )

time.sleep(1.2),print(Fore.CYAN+"[*]"+Fore.WHITE+"The Script is Running...")
time.sleep(1.2),print(Fore.CYAN+"[*]"+Fore.WHITE+"Preparing The Message...")
time.sleep(1.2),print(Fore.CYAN+"[*]"+Fore.WHITE+"Message sent successfully", message.sid)

