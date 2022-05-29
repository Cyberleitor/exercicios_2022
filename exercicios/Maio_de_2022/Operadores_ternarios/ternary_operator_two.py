def round(number): return number - (number % 10) + 10 if number % 10 >= 5 else number - (number % 10)
number = int(input('Informe o número para arredondar: '))
print(round(number))
