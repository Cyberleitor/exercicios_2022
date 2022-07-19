#!/usr/bin/env python3

import os
import time

def new_directory(directory, filename):
	if os.path.exists(directory) == False:
		os.mkdir(directory)

	os.chdir(directory)
	with open (filename, 'w') as file:
		pass
	os.chdir('..')
	return os.listdir(directory)

new_directory('PythonPrograms', 'script.py')

