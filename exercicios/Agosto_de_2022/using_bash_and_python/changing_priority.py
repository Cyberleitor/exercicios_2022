#!/bin/bash

for pid in $(pidof <process>); do
	renice 19 $pid
done
