#!/usr/bin/env python3

def find_the_unique_number(array):
	items_of_array = set(array)
	for index in items_of_array:
		if array.count(index) == 1:
			print(index)

find_the_unique_number([ 1, 1, 1, 2, 1, 1 ])
find_the_unique_number([ 0, 0, 0.55, 0, 0 ])
