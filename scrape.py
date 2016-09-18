import email
import mailbox
import os
from dateutil import parser
import datetime
import sys, re


dir_path = os.path.dirname(os.path.realpath(__file__))
file_path = os.path.join(os.sep, dir_path, sys.argv[1])
mbox = mailbox.mbox(file_path)

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