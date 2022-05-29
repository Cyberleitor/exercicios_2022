number = int(input('Digite o número do qual deseja descobrir o fatorial: '))

result = 1
counter = 1

while counter <= number:
    result *= counter
    counter += 1

print(f'O fatorial de {number} é {result}.')