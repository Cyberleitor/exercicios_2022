#!/bin/bash

# This script has the goal to encrypt information in cases of extremely necessary, just for security.

read -p "O que deseja criptografar? " objeto_criptografado
ccrypt -d -v -r $objeto_criptografado
echo "Processo finalizado."
