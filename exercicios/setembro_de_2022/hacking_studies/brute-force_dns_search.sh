#!/bin/bash

for url in $(cat dominios.txt); do
	host $url.$1 | ag "has address"
done
