#!/usr/bin/env python3

import csv

users =  [{'name': 'Sol Mansi', 'username': 'solm', 'departament': 'IT infrastructure'},
{'name': 'Lio Nelson', 'username': 'lion', 'departament': 'User Experience Research'},
{'name': 'Charlie Grey', 'username': 'greyc', 'departament': 'Development'}]
keys = ['name', 'username', 'departament']

with open('by_department.csv', 'w') as by_department:
	writer = csv.DictWriter(by_department, fieldnames=keys)
	writer.writeheader()
	writer.writerows(users)

