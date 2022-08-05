#!/bin/bash

for file in *.docx; do
	name=$(basename "$file" .docx)
	mv "$file" "$name.pdf"
done
