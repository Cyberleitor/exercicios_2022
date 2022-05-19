#!/usr/bin/env python
# coding: utf-8

# In[30]:


import numpy

tamanho = 4

matriz = numpy.empty([tamanho, tamanho])

for linha in range(0, tamanho):
    for coluna in range(0, tamanho):
        print('Informe o valor a ser inserido na linha e coluna ', linha,'/', coluna,':')
        matriz[linha][coluna] = int(input())

soma_linha = 0
soma_coluna = 0
soma_total = 0
for linha in range(0, tamanho):
    for coluna in range(0, tamanho):
        soma_total += matriz[linha][coluna]
        if linha == 1:
            soma_linha += matriz[linha][coluna]


print('A soma total dos integrantes da matriz é:', soma_total)
print('A soma dos integrantes da segunda linha da matriz é:', soma_linha)