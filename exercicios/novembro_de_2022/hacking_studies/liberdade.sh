#!/usr/bin/bash

for archive in ./*;
do
	mat2 -V --inplace "$archive"
done


