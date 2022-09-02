#!/usr/bin/env python3

def order_sentence(sentence):
	if sentence == "":
		print("")
	else:
		words_sentence = []
		for index in range(1, 10):
			for word in sentence.split():
				if str(index) in word:
					words_sentence.append(word)
		result = " ".join(words_sentence)
		print(result)


order_sentence("is2 Thi1s T4est 3a")
