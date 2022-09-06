#!/usr/bin/env python3

def mexican_wave(word):
	if word != " ":
		result = [word[:index].lower() + word[index].upper() + word[index+1:].lower() if word[index] != " " else " " for index in range(len(word))]
	else:
		result = word
	while " " in result:
		result.remove(" ")
	print(result)

mexican_wave("hello")
mexican_wave("Nothing")
mexican_wave("")
mexican_wave("Two words")
mexican_wave(" gap ")
mexican_wave( "    a     b     ")
