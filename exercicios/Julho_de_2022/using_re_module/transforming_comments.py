#!/usr/bin/env python3

import re

def transform_comments(line_of_code):
	result = re.sub('#+', '//', line_of_code)
	return result

print(transform_comments("### Start of program")) 

print(transform_comments("  number = 0   ## Initialize the variable")) 

print(transform_comments("  number += 1   # Increment the variable")) 

print(transform_comments("  return(number)"))

