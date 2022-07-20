#!/usr/bin/env python3

import csv

hosts = [['workstation.local', '000.000.00.00'], ['webserver.cloud','00.0.0.0']]

with open('hosts.csv', 'w') as hosts_csv:
	writer = csv.writer(hosts_csv)
	writer.writerows(hosts)

