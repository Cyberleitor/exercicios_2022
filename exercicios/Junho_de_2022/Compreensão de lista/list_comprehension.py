even_list = []
odd_list = []
size_list = int(input('Informe o tamanho desejado para a lista: '))
[even_list.append(index) if index % 2 == 0 else odd_list.append(index) for index in range(1, size_list + 1)]
print(f'Eis a lista dos pares: {even_list}.')
print(f'Eis a lista dos ímpares: {odd_list}.')
