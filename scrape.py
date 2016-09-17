import email
import mailbox
import os
import re

os.chdir('C:\Users\lycarter\Dropbox (MIT)\HackMIT2016')

mbox = mailbox.mbox('Reuse.mbox')

emailExtract = re.compile(r"(?P<email>\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,})")

senders = {}

for message in mbox:
	res = emailExtract.search(message['From'])
	if res:
		fromEmail = res.group('email')
	else:
		print message['From']
		fromEmail = ''
	senders[fromEmail] = senders.get(fromEmail, 0) + 1

sorted_senders = sorted(senders, key=senders.get, reverse=True)

print sorted_senders[:10]