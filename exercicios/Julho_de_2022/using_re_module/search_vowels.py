#!/usr/bin/env python3

import re

def multi_vowel_words(text):
	pattern = r'\w+[aiueo]{3,}\w+'
	result = re.findall(pattern, text)
	return result

print(multi_vowel_words("Life is beautiful")) 

print(multi_vowel_words("Obviously, the queen is courageous and gracious.")) 

print(multi_vowel_words("The rambunctious children had to sit quietly and await their delicious dinner.")) 

print(multi_vowel_words("The order of a data queue is First In First Out (FIFO)")) 

print(multi_vowel_words("Hello world!"))

