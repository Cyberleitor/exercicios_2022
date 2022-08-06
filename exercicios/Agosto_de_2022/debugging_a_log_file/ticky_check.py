#!/usr/bin/env python3

import sys, re, operator, csv

error_messages = {}
errors_for_users = {}
infos_for_users = {}

with open(sys.argv[1], 'r') as log_file:
	for line in log_file:
		error = re.search(r"ERROR ([\w ']*) \(", line)
		if error != None:
			error_entry = re.findall(r"ERROR ([\w ']*) \(", line)
			error_key = error_entry[0]
			if error_key in error_messages.keys():
				error_messages[error_key] += 1
			else:
				error_messages[error_key] = 1

			user = re.findall(r"\(([\w.]*)\)", line)
			user_key = user[0]
			if user_key in infos_for_users.keys():
				errors_for_users[user_key] += 1
			else:
				errors_for_users[user_key] = 1

			if user_key not in infos_for_users.keys():
				infos_for_users[user_key] = 0

		information = re.search(r"INFO", line)
		if information != None:
			user_entry = re.findall(r"\(([\w.]*)\)", line)
			user_key = user_entry[0]
			if user_key in infos_for_users.keys():
				infos_for_users[user_key] += 1
			else:
				infos_for_users[user_key] = 1

			if user_key not in errors_for_users.keys():
				errors_for_users[user_key] = 0

with open('error_message.csv', 'w') as error_file:
	first_writer = csv.writer(error_file)
	header = ['Error', 'Count']
	first_writer.writerow(header)
	indexes = sorted(error_messages.items(), key = operator.itemgetter(1), reverse = True)
	for index in indexes:
		line = [index[0], index[1]]
		first_writer.writerow(line)

with open('user_statistics.csv', 'w') as info_file:
	second_writer = csv.writer(info_file)
	header = ['Username', 'INFO', 'ERROR']
	second_writer.writerow(header)
	indexes = sorted(infos_for_users.items())
	for index in indexes:
		line = [index[0], index[1], errors_for_users[index[0]]]
		second_writer.writerow(line)

