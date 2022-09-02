#!/usr/bin/env python3

def bit_counting(number):
	result = format(number, "b")
	if number < 0:
		print("Número negativo")
	else:
		print(result.count("1"))

bit_counting(-15)
bit_counting(0)
bit_counting(4)
bit_counting(10)
bit_counting(1234)
