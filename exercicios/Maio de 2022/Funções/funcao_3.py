#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def gasto_combustivel():
    
    print('Qual é o tempo estimado para a viagem em horas?')
    tempo_viagem = float(input())
    print('Qual é a velocidade média para a viagem?')
    velocidade_media = float(input())
    print('Quantos quilômetros por litro de gasolina o veículo é capaz de fazer?')
    quilometros_viagem = float(input())
    
    distancia_viagem = tempo_viagem * velocidade_media
    gasolina_viagem = distancia_viagem / quilometros_viagem
    
    print('Com a velocidade média de',velocidade_media,'km/h, o tempo de',tempo_viagem,'horas de deslocamento e a distância de',distancia_viagem,'quilômetros, serão gastos',gasolina_viagem,'litros de gasolina.')
    
if __name__ == '__main__':
    
    gasto_combustivel()

