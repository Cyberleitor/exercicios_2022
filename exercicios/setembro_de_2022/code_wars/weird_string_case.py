#!/usr/bin/env python3

def weird_string_case(words):
	result = []
	for word in words.split():
		final_phrase = ""
		for letter in range(len(word)):
			if letter % 2 == 0:
				final_phrase += word[letter].upper()
			else:
				final_phrase += word[letter].lower()
		result.append(final_phrase)
	print(' '.join(result))


weird_string_case("String")
weird_string_case("Weird string case")
