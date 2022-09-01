#!/usr/bin/env python3

def is_this_triangle(a, b, c):
	if b + c > a and a + c > b and a + b > c:
		print(True)
	else:
		print(False)

is_this_triangle(5, 10, 9)
is_this_triangle(7, 2, 2)
