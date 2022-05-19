# Objetivo:
# Dados 'n' nomes e números de telefones, monte um caderno de telefones que relaciona os nomes de amigos a seus respectivos números de telefone;
# Você então receberá um número desconhecido de nomes para consultar em sua lista telefônica;
# Para cada nome consultado, print a entrada associada em sua lista telefônica em uma nova linda na forma 'name=phoneNumber';
# Se a entrada para 'name' não é encontrada, print 'Not found'.

# Nota: sua lista telefônica deve ser um dicionário.

# Formato de input:
# A primeira linha contém um inteiro, 'n', denotando o número de entradas na lista telefônica;
# Cada uma das 'n' subsequentes linhas descreve uma entrada no formato de dois valores separados por espaço em uma única linha;
# O primeiro valor é o nome de um amigo e o segundo valor é um número de telefone de 8 dígitos;
# Depois das 'n' linhas de entradas na lista telefônica, existe um número desconhecido de linhas de busca;
# Cada linha (consulta) contém uma pesquisa e você deve continuar lendo as linhas até que não haja mais entrada.

# Nota: 'names' consistêm em letras em caixa baixa do alfabeto inglês e são apenas primeiros nomes.
# Restrições: 1 <= n <= 10^5 / 1<= queries <= 10^5

# Formato de output: Uma linha para cada consulta, print 'Not found' se o 'name' não tem uma correspondência;
# De outra maneira, print o 'name' completo e o 'phoneNumber' no formato name=phoneNumber.

import sys

phone_list = int(sys.stdin.readline().strip())
phone_book = dict()

for index in range(0, phone_list):
    contact_friends = sys.stdin.readline().strip().split(' ')
    phone_book[contact_friends[0]] = contact_friends[1]

search = sys.stdin.readline().strip()
while search:
    phoneNumber = phone_book.get(search)
    if phoneNumber:
        print(search + "=" + phoneNumber)
    else:
        print('Not found')
    search = sys.stdin.readline().strip()