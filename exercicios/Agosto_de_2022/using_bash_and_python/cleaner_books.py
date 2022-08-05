#!/usr/bin/env python3

import os
import subprocess

for file in os.listdir('.'):
	if '.pdf' in file:
		subprocess.run(['srm','-vf', f'{file}'])
	elif '.mobi' in file:
		subprocess.run(['srm','-vf', f'{file}'])
	elif '.epub' in file:
		subprocess.run(['srm','-vf', f'{file}'])
	elif '.azw3' in file:
		subprocess.run(['srm','-vf', f'{file}'])
	else:
		pass
