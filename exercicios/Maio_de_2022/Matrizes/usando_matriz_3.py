#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy

tamanho = 3

matriz_a = numpy.empty([tamanho, tamanho])

for linha in range(0, tamanho):
    for coluna in range(0, tamanho):
        print('Informe o valor a ser inserido na matriz "a", linha', linha, 'e coluna', coluna,':')
        matriz_a[linha][coluna] = int(input())

matriz_b = numpy.empty([tamanho, tamanho])
for linha in range(0, tamanho):
    for coluna in range(0, tamanho):
        print('Informe o valor a ser inserido na matriz "b", linha', linha, 'e coluna', coluna,':')
        matriz_b[linha][coluna] = int(input())
        
matriz_c = matriz_a + matriz_b

print(matriz_c)