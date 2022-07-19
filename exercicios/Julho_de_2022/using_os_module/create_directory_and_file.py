#!/usr/bin/env python3

import os

def create_python_script(filename):
	comments = "# Start of a new Python program"
	with open('program.py', 'w') as script:
		script.write(comments)
		filesize = script
	return(os.path.getsize(filename))

print(create_python_script("program.py"))

