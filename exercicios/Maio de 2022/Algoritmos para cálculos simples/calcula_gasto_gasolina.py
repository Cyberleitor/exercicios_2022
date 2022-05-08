print('Informe o tempo estimado (em horas) para efetuar a viagem...')
tempo = float(input())
print('Informe a velocidade média (em quilômetros) estimada para a viagem...')
velocidade_media = float(input())
print('Informe quantos quilômetros por litro de gasolina são percorridos pelo veículo ...')
quilometro_consumo = float(input())

distancia = tempo * velocidade_media
litros_usados = distancia / quilometro_consumo

print('Considerando a velocidade média de ' + str(velocidade_media) + ' km/h e o tempo de ' + str(tempo) + ' h gasto para o deslocamento, serão necessários ' + str(litros_usados) + ' litros de gasolina.')