#!/usr/bin/env python3

def binary_search(list, key):
	list.sort()
	left = 0
	right = len(list) - 1

	while left <= right:
		middle = (left + right) // 2
		if list[middle] == key:
			return middle
		if list[middle] > key:
			print('Checking the left side')
			right = middle - 1
		if list[middle] < key:
			print('Checking the right side')
			left = middle + 1
	return -1

