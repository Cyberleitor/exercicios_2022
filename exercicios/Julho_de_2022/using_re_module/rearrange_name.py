#!/usr/bin/env python3

import re

def rearrange_name(name):
	result = re.search(r'^([\w \.-]+), ([\w \.-]+)$', name)
	result.groups()
	print(f'{result[2]} {result[1]}')

rearrange_name('Lovelace, Ada')
rearrange_name('Hopper, Grace M.')

# The output:
# Ada Lovelace
# Grace M. Hopper

