#!/usr/bin/env python3

the_first_list = [19, 5, 42, 2, 77]
the_second_list = [10, 343445353, 3453445, 3453545353453]

def sum_two_smallest_numbers(numbers):
	numbers.sort()
	result = numbers[0] + numbers[1]
	print(result)

sum_two_smallest_numbers(the_first_list)
sum_two_smallest_numbers(the_second_list)
