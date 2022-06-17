the_list = [[],[]]
cities = 0

answer = str(input('Você quer cadastrar uma nova pessoa na lista (y/n)? ').lower())
while answer not in 'yn':
    print('Por favor, responda "y" (sim) ou "n" (não).')
    answer = str(input('Você quer cadastrar uma nova pessoa na lista (y/n)? ').lower())
while answer == 'y':
    new_name = str(input('Informe o nome da pessoa: '))
    the_list[0].append(new_name)
    new_city = str(input('Informe a cidade em que essa pessoa reside: '))
    the_list[1].append(new_city)
    answer = str(input('Você quer cadastrar uma nova pessoa na lista (y/n)? ').lower())

for name in the_list[0]:
    print(f'{name} reside em {the_list[1][cities]}.')
    cities += 1