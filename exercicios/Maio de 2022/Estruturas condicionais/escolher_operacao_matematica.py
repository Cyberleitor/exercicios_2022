print('Digite o primeiro número da operação...')
primeiro_numero = float(input())
print('Digite o segundo número da operação...')
segundo_numero = float(input())
print('Você quer somar, subtrair, multiplicar ou dividir os números fornecidos?')
operacao = input()

soma = primeiro_numero + segundo_numero
subtracao = primeiro_numero - segundo_numero
multiplicacao = primeiro_numero * segundo_numero
divisao = primeiro_numero / segundo_numero

if operacao.lower() == 'somar':
    print(primeiro_numero,'+',segundo_numero,'é igual a ',soma,'.')
elif operacao.lower() == 'subtrair':
    print(primeiro_numero, '-',segundo_numero,'é igual a ',subtracao, '.')
elif operacao.lower() == 'multiplicar':
    print(primeiro_numero, 'x',segundo_numero,'é igual a ',multiplicacao, '.')
elif operacao.lower() == 'dividir':
    print(primeiro_numero, '/',segundo_numero,'é igual a ',divisao, '.')
else:
    print('Reinicie o algoritmo e indique uma operação válida.')