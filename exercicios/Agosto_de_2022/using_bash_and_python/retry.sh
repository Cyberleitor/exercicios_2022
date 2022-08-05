#!/bin/bash

number=0
command=$1

while ! $command && [ $number -le 5 ]; do
	sleep $number
	((number+=1))
	echo "Retry #$number"
done;
