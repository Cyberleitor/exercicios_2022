#!/bin/bash

read -p "Qual é o arquivo que deseja codificar com o base64? " arquivo
read -p "Qual é o nome do arquivo em que deseja guardar o hash? " codificado
cat $arquivo | base64 > $codificado
echo "Procedimento finalizado."

