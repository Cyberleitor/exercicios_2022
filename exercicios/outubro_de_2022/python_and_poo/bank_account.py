#!/usr/bin/env python3

import datetime

class Cliente:

	def __init__(self, nome, sobrenome, cpf):
		self.nome = nome
		self.sobrenome = sobrenome
		self.cpf = cpf

class Conta:

	_total_contas = 0

	def __init__(self, numero, cliente, saldo):
		self.numero = numero
		self.cliente = cliente
		self.saldo = saldo
		Conta._total_contas += 1
		self.historico = Historico()

	@staticmethod
	def get_total_contas():
		return Conta._total_contas

	def depositar(self, valor):
		self.saldo += valor
		self.historico.transacoes.append("Depósito de {}".format(valor))

	def sacar(self, valor):
		if self.saldo < valor:
			return False
		else:
			self.saldo -= valor
			self.historico.transacoes.append("Saque de {}".format(valor))

	def extrato(self):
		print("Número: {} \nSaldo: {}".format(self.numero, self.saldo))
		self.historico.transacoes.append("Tirou extrato - Saldo de {}".format(self.saldo))

	def transferir(self, destino, valor):
		retirar = self.sacar(valor)
		if retirar == False:
			return False
		else:
			destino.depositar(valor)
			self.historico.transacoes.append("Transferência de {} para a conta {}".format(valor, destino.numero))
			return True

class Historico:

	def __init__(self):
		self.data_abertura = datetime.datetime.today()
		self.transacoes = []

	def imprimir(self):
		print(f"Data de abertura: {self.data_abertura}")
		print("Transações: ")
		for transacao in self.transacoes:
			print("-", transacao)

cliente_um = Cliente('João', 'Oliveira', '11111111111-11')
cliente_dois = Cliente('José', 'Azevedo', '222222222-22')
conta_um = Conta('123-4', cliente_um, 1000.0)
conta_dois = Conta('123-5', cliente_dois, 1000.0)
conta_um.depositar(100.0)
conta_um.sacar(50.0)
conta_um.transferir(conta_dois, 200.0)
conta_um.extrato()
conta_um.historico.imprimir()
conta_dois.historico.imprimir()
criar_cliente_um = Cliente('John', 'Nada', '333333333-33')
criar_cliente_dois = Cliente('Jane', 'Doe', '444444444-44')
criar_conta_um = Conta('123-6', criar_cliente_um, 1000.0)
criar_conta_dois = Conta('123-7', criar_cliente_dois, 1000.0)
print(f"Total de contas: {Conta.get_total_contas()}")

