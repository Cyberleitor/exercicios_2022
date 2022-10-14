#!/usr/bin/env python3

import random

# This script was writen while I read a book about Python and POO (starting with the basis of the programming language and advancing toward more complex exercises).

print("*" * 41)
print("*" + " " * 10 + "Jogo da adivinhação" + " " * 10 + "*")
print("*" * 41)

class Adivinhacao():
	def __init__(self):
		self.numero = random.randint(1, 100)
		self.chute = int(input("Dentro de uma faixa de números inteiros de 1 a 100, qual você acredita que é o valor misterioso? "))

	def apresentar_resultado(self):
		resultado = self.numero == self.chute
		match resultado:
			case True:
				print(f"Você acertou! {self.chute} era o valor misterioso.")
			case False:
				print(f"Você errou! O valor misterioso era {self.numero}.")

	def continuar_ou_parar(self):
		self.pergunta = input("Você deseja continuar a jogar (sim/não)? ")
		resposta = self.pergunta
		match resposta.lower():
			case "sim":
				jogo = Adivinhacao()
				jogo.apresentar_resultado()
				jogo.continuar_ou_parar()
			case "não":
				print("Certo, até outro momento...")

jogo = Adivinhacao()
jogo.apresentar_resultado()
jogo.continuar_ou_parar()

