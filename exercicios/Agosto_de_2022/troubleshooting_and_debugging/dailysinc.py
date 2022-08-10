#!/usr/bin/env python3

import subprocess
from multiprocessing import Pool
import os

def backup(src):
	dest = os.getcwd() + "/data/prod_backup/"
	subprocess.call(["rsync", "-arq", src, dest])

if __name__ == '__main__':
	src = os.getcwd() + '/data/prod/'
	the_files = os.listdir(src)
	list_of_files = []
	for archive in the_files:
		the_path = os.path.join(src, archive)
		list_of_files.append(the_path)

	with Pool(len(list_of_files)) as pool:
		pool.map(backup, list_of_files)

