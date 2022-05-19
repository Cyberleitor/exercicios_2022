lista_numeros = [1, 2, -3, 4, -5, 6, 7, -8, -9, 10, -11, 12, -13]
num = 0
numeros_negativos = 0

while num < len(lista_numeros):

    if lista_numeros[num] < 0:
        numeros_negativos += 1

    num += 1

print('Na lista, existem',numeros_negativos,'números negativos.')