import time

resposta = 's'

while resposta == 's':

    print('Informe o comprimento da caixa...')
    comprimento_caixa = float(input())
    print('Informe a largura da caixa...')
    largura_caixa = float(input())
    print('Informe a altura da caixa...')
    altura_caixa = float(input())

    volume_caixa = comprimento_caixa * largura_caixa * altura_caixa

    print('O volume da caixa é: ', volume_caixa, '.')

    time.sleep(1)

    print('Você deseja fazer um novo cálculo de volume (s/n)?')
    resposta = input()