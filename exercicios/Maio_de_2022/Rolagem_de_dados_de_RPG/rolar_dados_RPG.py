import random
import time

dados_quantidade = 0

dados_tipo = str(input('Qual tipo de dado você quer rolar (d4, d6, d8, d10, d12 ou d20)? ')).strip()
while dados_tipo not in 'd4 d6 d8 d10 d12 d20' or dados_tipo in '4 6 8 10 12 20 d1 d2 0':
    print('Por favor, informe uma das opções válidas (d4, d6, d8, d10, d12 ou d20).')
    dados_tipo = str(input('Qual tipo de dado você quer rolar? ')).strip()

match dados_tipo:
    case 'd4':
        dados_tipo = 1
    case 'd6':
        dados_tipo = 2
    case 'd8':
        dados_tipo = 3
    case 'd10':
        dados_tipo = 4
    case 'd12':
        dados_tipo = 5
    case 'd20':
        dados_tipo = 6

time.sleep(0.01)

while dados_quantidade not in range(1, 1000):
    try:
        dados_quantidade = int(input('Quantos dados você quer rolar (digite um número inteiro – por exemplo: 7 – entre 1 e 1.000)? '))
    except ValueError:
        print('A quantidade de dados deve ser um número inteiro.')

time.sleep(0.01)
    
for item in range(dados_quantidade):
    match dados_tipo:
        case 1:
            print(random.randint(1, 4))
        case 2:
            print(random.randint(1, 6))
        case 3:
            print(random.randint(1, 8))
        case 4:
            print(random.randint(1, 10))
        case 5:
            print(random.randint(1, 12))
        case 6:
            print(random.randint(1, 20))