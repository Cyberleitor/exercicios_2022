#!/usr/bin/env python3

import csv

file_csv = open('csv_file.txt')
reading_csv = csv.reader(file_csv)

for row in reading_csv:
	character,movie,director = row
	print(f'Character: {character} | Movie: {movie} | Director: {director}')

file_csv.close()

