#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def repetir():
    
    print('Digite a palavra que deseja repetir...')
    palavra_repetida = input()
    print('Quantas vezes você quer que a palavra seja repetida?')
    quantidade_repeticao = int(input())
    
    print(palavra_repetida * quantidade_repeticao)

if __name__ == '__main__':
    
    repetir()

