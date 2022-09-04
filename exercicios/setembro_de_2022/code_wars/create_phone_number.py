#!/usr/bin/env python3

def create_phone_number(array):
	region_code = "".join(map(str, array[:3]))
	first_part_number = "".join(map(str, array[3:6]))
	second_part_number = "".join(map(str, array[6:]))
	print(f"({region_code}) {first_part_number}-{second_part_number}")


create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
