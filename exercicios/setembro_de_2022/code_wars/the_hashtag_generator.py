#!/usr/bin/env python3

import re

def the_hashtag_generator(phrase):
	phrase_result = "#" + phrase.replace(" ", "")
	print(phrase_result)


the_hashtag_generator(" Hello there thanks for trying my Kata")
the_hashtag_generator("    Hello     World   ")
