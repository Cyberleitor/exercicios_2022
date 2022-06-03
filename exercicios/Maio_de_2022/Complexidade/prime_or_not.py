# Algorithm to discover if a number is prime or not.

print('Quantos testes você quer fazer? ')
tests = int(input())

while tests > 0:

    print('Qual número deseja descobrir se é primo? ')
    number = int(input())
    counter = 0

    for index_two in range(1, number + 1):
        if number % index_two == 0:
            counter += 1
        else:
            counter = counter

    if counter == 2:
        print('Prime')
    else:
        print('Not prime')

    tests -= 1
