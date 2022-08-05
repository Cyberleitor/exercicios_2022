#!/bin/bash

for logfile in /var/log/syslog; do
	echo "Processing: $logfile"
	cut -d' ' -f5- $logfile | sort | uniq -c | sort -nr | head -5
done
