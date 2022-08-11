#!/usr/bin/env python3

from memory_profiler import profile

@profile
def calculating(number_one,number_two):
	result = number_one * number_two
	print(result)

calculating(8,3)
