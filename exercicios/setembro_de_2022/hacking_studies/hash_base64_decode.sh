#!/bin/bash

read -p "Qual é o arquivo que deseja decodificar com o base64? " codificado
read -p "Qual é o nome do arquivo em que deseja guardar a informação decodificada? " decodificado
cat $codificado | base64 -d > $decodificado
echo "Procedimento finalizado."

