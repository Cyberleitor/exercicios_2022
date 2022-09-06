#!/usr/bin/env python3

def alphabet_position(text):
	alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
		"k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
		"u", "v", "w", "x", "y", "z"]
	indexes_letters = []
	for letter in text.lower():
		if letter in alphabet:
			indexes_letters.append(str(alphabet.index(letter) + 1))
	print(" ".join(indexes_letters))


alphabet_position("The sunset sets at twelve o' clock.")
