print('Digite a sua idade: ')
fase_idade = int(input())

if fase_idade <= 12:
    print('Você é uma criança.')
elif fase_idade > 18:
    print('Você é um adulto.')
else:
    print('Você é um adolescente.')