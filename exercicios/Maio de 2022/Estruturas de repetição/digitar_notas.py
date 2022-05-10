print('Digite a primeira nota...')
primeira_nota = float(input())

while primeira_nota < 0 or primeira_nota > 10:
    print('Digite a primeira nota...')
    primeira_nota = float(input())

print('Digite a segunda nota...')
segunda_nota = float(input())

while segunda_nota < 0 or segunda_nota > 10:
    print('Digite a segunda nota...')
    segunda_nota = float(input())

media_notas = float((primeira_nota + segunda_nota) / 2)

print('A média das duas notas é: ',media_notas)