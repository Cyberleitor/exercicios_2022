#!/usr/bin/env python3

def spining_words(sentence):
	words_of_phrase = sentence.split(" ")
	phrase_with_word_spined = []
	for index in words_of_phrase:
		if len(index) > 5:
			index = index[::-1]
			phrase_with_word_spined.append(index)
		else:
			phrase_with_word_spined.append(index)
		the_result = " ".join(phrase_with_word_spined)
	print(the_result)

spining_words("Hey fellow warriors")
spining_words("This is a test")
spining_words("This is another test")
