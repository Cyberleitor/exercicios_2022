#!/bin/bash

#requerimento: steghide version 0.5.1
#Um script simples para praticar esteganografia.

read -p "De qual imagem deseja extrair a mensagem oculta (informe a extensão)? " oculto
read -p "Qual deve ser o nome do arquivo com a mensagem (informe a extensão)? " mensagem
steghide extract -sf $oculto -xf $mensagem
echo "Procedimento finalizado."

