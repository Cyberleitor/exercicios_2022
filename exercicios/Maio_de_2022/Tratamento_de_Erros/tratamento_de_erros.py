import time

list_numbers = []

print('Quantos números você deseja inserir na lista?')
contagem = int(input())
number_order = int(1)

time.sleep(0.01)

while contagem > 0:
    try:
        print(f'Informe o {number_order}º número que deseja inserir na lista: ')
        number = int(input())
        number_order += 1
        contagem -= 1
        list_numbers.append(number)
    except ValueError:
        print('Erro de valor: por favor, informe um valor numérico.')
    except ZeroDivisionError:
        print('Erro de divisão: por favor, informe um valor acima de 0.')
    except IndexError:
        print('Erro de índice: por favor, informe um índice que exista na lista.')
    except KeyboardInterrupt:
        print('Erro de execução: o usuário interrompeu a execução do programa.')

time.sleep(0.01)

print(f'A sua lista ficou assim: {list_numbers}.')