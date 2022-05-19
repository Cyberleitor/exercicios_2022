print('Informe o primeiro número da operação matemática...')
primeiro_numero = float(input())
print('Informe o segundo número da operação matemática...')
segundo_numero = float(input())
print('Você quer somar, multiplicar, subtrair ou dividir?')
operacao_matematica = str(input())

if operacao_matematica.lower() == 'somar':
    soma = primeiro_numero + segundo_numero
    print('A soma dos números fornecidos é:',soma)
elif operacao_matematica.lower() == 'multiplicar':
    multiplica = primeiro_numero * segundo_numero
    print('A multiplicação dos números fornecidos é:',multiplica)
elif operacao_matematica.lower() == 'subtrair':
    subtrai = primeiro_numero - segundo_numero
    print('A subtração dos números fornecidos é:',subtrai)
elif operacao_matematica.lower() == 'dividir':
    divide = primeiro_numero / segundo_numero
    print('A divisão dos números fornecidos é:',divide)