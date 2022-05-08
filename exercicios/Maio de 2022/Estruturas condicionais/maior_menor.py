print('Digite o primeiro número da comparação...')
primeiro_numero = float(input())
print('Digite o segundo número da comparação...')
segundo_numero = float(input())


if primeiro_numero > segundo_numero:
    print(primeiro_numero,'é maior do que',segundo_numero,'.')
elif segundo_numero > primeiro_numero:
    print(segundo_numero,'é maior do que',primeiro_numero,'.')
else:
    print(primeiro_numero,'e',segundo_numero,'possuem valor igual.')