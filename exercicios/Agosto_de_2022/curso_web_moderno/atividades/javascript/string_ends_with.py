#!/usr/bin/env python3

def string_ends_with(string, ending):
	if string.endswith(ending) or ending == "":
		print(True)
	else:
		print(False)

string_ends_with("abcde", "cde")
string_ends_with("abcde", "abc")
string_ends_with("abcde", "")
