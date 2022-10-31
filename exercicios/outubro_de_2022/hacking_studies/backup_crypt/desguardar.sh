#!/usr/bin/bash

read -p "Qual é o arquivo que deseja acessar? " arquivo;
read -sp "Qual é a senha do arquivo? " senha;
dd if=$arquivo | openssl aes256 -d -k $senha | tar xvzf -

