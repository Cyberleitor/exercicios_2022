#!/usr/bin/env python3

from bank_account import ContaCorrente

def metodo_um():
	print("Início do método um.")
	metodo_dois()
	print("Fim do método dois.")

def metodo_dois():
	print("Início do método dois.")
	conta_corrente = ContaCorrente("123-4", "Maria", 0)
	try:
		for index in range(1, 15):
			conta_corrente.depositar(index + 1000)
			print(conta_corrente._saldo)
			if index == 5:
				conta_corrente = None
	except:
		print("Erro.")

	print("Fim do método dois.")

if __name__ == '__main__':
	print("Início do main.")
	metodo_um()
	print("Fim do main.")

