print('Digite o nome do aluno: ')
nome_aluno = input()
print('Informe a primeira nota do aluno: ')
nota1 = float(input())
print('Informe a segunda nota do aluno: ')
nota2 = float(input())
print('Informe a terceira nota do aluno: ')
nota3 = float(input())
print('Informe a quarta nota do aluno: ')
nota4 = float(input())

media_notas = (nota1 + nota2 + nota3 + nota4) / 4

if media_notas >= 6:
    print(nome_aluno + ' foi aprovado com a média: ', media_notas)
else:
    print(nome_aluno + ' foi reprovado com a média: ', media_notas)