#!/bin/bash

#requerimento: steghide version 0.5.1
#Um script simples para praticar esteganografia. 

read -p "Qual é o arquivo com a mensagem a ser ocultada (informe a extensão)? " mensagem
read -p "Em qual imagem deseja ocultar a mensagem (informe a extensão)? " imagem
read -p "Qual deve ser o nome da imagem com mensagem oculta (informe a mesma extensão da imagem original)? " oculto
steghide embed -ef $mensagem -cf $imagem -sf $oculto
echo "Procedimento finalizado."

