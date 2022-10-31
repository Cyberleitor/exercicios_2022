#!/usr/bin/bash

read -p "Qual é o arquivo ou diretório que deseja guardar com segurança? " arquivo;
read -sp "Qual é a senha que deseja para o arquivo ou diretório guardado? " senha;
tar -zcvf - $arquivo | openssl aes256 -salt -k $senha | dd of=$arquivo.seguro


