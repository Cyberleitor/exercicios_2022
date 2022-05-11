#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy

tamanho = 3
numero_quantidade = 0

matriz = numpy.empty([tamanho, tamanho])

for linha in range(0, tamanho):
    for coluna in range(0, tamanho):
        print('Informe o valor a ser inserido na linha e coluna ', linha,'/',coluna,':')
        matriz[linha][coluna] = int(input())

print('Digite um número e descubra se ele está na matriz...')
numero = int(input())

for linha in range(0, tamanho):
    for coluna in range(0, tamanho):
        if matriz[linha][coluna] == numero:
            numero_quantidade += 1

print('O número',numero,'aparece na matriz',numero_quantidade,'vezes.')