#!/usr/bin/env python3

import re
import sys

logfile = sys.argv[1]
usernames = {}

with open(logfile) as file:
	for line in file:
		if 'CRON' not in line:
			continue
		pattern_to_search = r'USER \((\w+)\)$'
		users_list = re.search(pattern_to_search, line)
		if result is None:
			continue
		name = result[1]
		usernames[name] = usernames.get(name, 0) + 1
print(usernames)
