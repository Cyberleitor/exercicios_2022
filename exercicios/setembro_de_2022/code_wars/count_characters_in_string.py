#!/usr/bin/env python3

def count_characters_in_string(string):
	result = {}
	if string == "":
		pass
	else:
		for index in string.lower():
			if index not in result:
				result[index] = 1
			else:
				result[index] += 1
	print(result)


count_characters_in_string("aba")
count_characters_in_string("Happiness")
count_characters_in_string("Another")
count_characters_in_string("reality")
count_characters_in_string("frequencies")
count_characters_in_string("")
