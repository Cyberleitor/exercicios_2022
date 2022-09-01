#!/usr/bin/env python3

first_array = [1, 1, 2]
second_array = [0, 1, 0, 1, 0]
third_array = [1, 2, 2, 3, 3, 3, 4, 3, 3, 3, 2, 2, 1]
fourth_array = [-5, 2, -1, 9, -5, 10, 2, 9, 2, -1, 2, 10, -5, 2, 9, 9, 2]

def finding_odd_occurrences_number(array):
	counting_ocurrences = dict((index, array.count(index)) for index in array)
	for index in counting_ocurrences:
		if array.count(index) % 2 != 0:
			print(index)

finding_odd_occurrences_number(first_array)
finding_odd_occurrences_number(second_array)
finding_odd_occurrences_number(third_array)
finding_odd_occurrences_number(fourth_array)
