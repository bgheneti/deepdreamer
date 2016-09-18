import email
import mailbox
import os
from dateutil import parser
import datetime
from datetime import timezone
import sys

mbox = mailbox.mbox(sys.argv[1])

dates = [message.get("Date") for message in mbox]

def boom(dt):
	return dt.replace(tzinfo=timezone.utc).astimezone(tz=None)

freq = [[0 for col in range(24)] for row in range(7)]

for date in dates:
	try:
		parsed_date = boom(parser.parse(date))
		freq[parsed_date.weekday()][parsed_date.hour] += 1
	except:
		continue

print(*range(24), sep='\t')
print('\n')

for row in freq:
	print(*row, sep='\t')
42