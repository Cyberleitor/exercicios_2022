#!/usr/bin/env python3

import sys
import subprocess

file = sys.argv[1]

with open(file) as text:
        for line in text.readlines():
                the_line = line.strip()
                old_nick = 'jane'
                new_nick = the_line.replace(old_nick, 'jdoe')
                subprocess.run(['mv', the_line, new_nick])

text.close()
