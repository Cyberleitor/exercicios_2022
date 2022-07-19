#!/usr/bin/env python3

import os
import datetime

def file_date(filename):
	with open (filename, 'w') as file:
		pass
	timestamp = os.path.getmtime(filename)
	modification_date = datetime.datetime.fromtimestamp(timestamp).date()
	return (f'{modification_date}')

print(file_date('newfile.txt'))

