#!/usr/bin/env python3

import os

for arquivo in os.listdir():
	os.rename(arquivo, arquivo.lower().replace(' ','_'))
