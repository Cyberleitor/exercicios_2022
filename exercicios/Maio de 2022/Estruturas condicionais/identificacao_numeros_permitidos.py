print('Informe um número entre 0 e 9...')
numero_permitido = int(input())

if numero_permitido < 0:
    print(numero_permitido,'não está entre os números permitidos.')
elif numero_permitido > 9:
    print(numero_permitido, 'não está entre os números permitidos.')
else:
    print(numero_permitido, 'está entre os números permitidos.')