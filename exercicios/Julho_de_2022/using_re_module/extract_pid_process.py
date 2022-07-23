#!/usr/bin/env python3

import re

def extract_pid(log_line):
	regex = r'\[(\d+)\]'
	result = re.search(regex, log_line)
	if result is None:
		return ''
	return result[1]

print(extract_pid('The pid is [123456] for the program xxxxxx.'))

