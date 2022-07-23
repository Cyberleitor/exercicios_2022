#!/usr/bin/env python3

import re

def transform_record(record):
	new_record = re.sub(r',(\d{3})', r',+1-\1', record)
	return new_record

print(transform_record("Sabrina Green,802-867-5309,System Administrator")) 

print(transform_record("Eli Jones,684-3481127,IT specialist")) 

print(transform_record("Melody Daniels,846-687-7436,Programmer")) 

print(transform_record("Charlie Rivera,698-746-3357,Web Developer")) 

