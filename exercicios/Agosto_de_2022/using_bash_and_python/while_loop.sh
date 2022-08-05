#!/bin/bash

number=1
while [ $number -le 5 ]; do
	echo  "Iteration number $number"
	((number+=1))
done
