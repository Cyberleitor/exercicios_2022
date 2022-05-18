# Objetivo:
# Usar recursão para calcular fatorial.

# # Parâmetros:
# 'n': um número inteiro.

# #Retorno:
# int: o fatorial de n.

# Input:
# um único inteiro, 'n' (o argumento a passar ao fatorial).

# Restrições:
# 2 <= 'n' <=12;
# Sua submissão deve conter uma função recursiva chamada fatorial.

import math
import os
import random
import re
import sys

def factorial(n):

    return 1 if (n == 0 or n == 1) else n * factorial(n -1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = factorial(n)

    fptr.write(str(result) + '\n')

    fptr.close()