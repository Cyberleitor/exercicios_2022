#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def celsius_farenheit():
    
    print('Qual é a temperatura que deseja converter de celsius para farenheit?')
    temperatura_celsius = float(input())
    
    temperatura_farenheit = (temperatura_celsius * 9 / 5) + 32
    
    print('Convertida para farenheit, a temperatura informada corresponde a:', temperatura_farenheit)
    
if __name__ == '__main__':
    
    celsius_farenheit()

