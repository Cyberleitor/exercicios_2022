#!/usr/bin/env python3

import datetime
import abc

class AutenticacaoMixIn:

	def autenticacao(self, senha):
		pass

class SistemaInterno:

	def login(self, obj):
		if hasattr(obj, "autenticacao"):
			obj.autenticacao()
			return True
		else:
			print(f"A instância {obj.__class__.__name__} não é autenticável.")
			return False

class AtendimentoMixIn:

	def cadastrar_atendimento(self):
		pass

	def atender_cliente(self):
		pass

class HoraExtraMixIn:

	def calcular_hora_extra(self, horas):
		pass

class TributavelMixIn:

	def get_valor_imposto(self):
		pass

class Cliente(AutenticacaoMixIn):

	def __init__(self, nome, cpf, senha):
		self._nome = nome
		self._cpf = cpf
		self._senha = senha

class Conta(abc.ABC):

	_total_contas = 0

	def __init__(self, numero, cliente, saldo):
		self._numero = numero
		self._cliente = cliente
		self._saldo = saldo
		Conta._total_contas += 1
		self.historico = Historico()

	@abc.abstractmethod
	def definir_tipo_taxa():
		pass

	@staticmethod
	def get_total_contas():
		return Conta._total_contas

	def depositar(self, valor):
		self._saldo += valor
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

class ContaCorrente(Conta, TributavelMixIn):

	def definir_tipo_taxa(self, taxa):
		self._saldo += self._saldo * taxa * 2

	def depositar(self, valor):
		self._saldo += valor - 0.10

	def get_valor_imposto(self):
		return self._saldo * 0.01

class ContaPoupanca(Conta):

	def definir_tipo_taxa(self, taxa):
		self._saldo += self._saldo * taxa * 3

class ContaInvestimento(Conta):

	def definir_tipo_taxa(self, taxa):
		self._saldo += self._saldo * taxa * 5

class SeguroDeVida(TributavelMixIn):

	def __init__(self, valor, titular, numero_apolice):
		self._valor = valor
		self._titular = titular
		self._numero_apolice = numero_apolice

	def get_valor_imposto(self):
		return 42 + self._valor * 0.05

class ManipuladorDeTributaveis:

	def calcular_impostos(self, lista_tributaveis):
		total = 0
		for tributo in lista_tributaveis:
			total += tributo.get_valor_imposto()
		return total

class Historico:

	def __init__(self):
		self.data_abertura = datetime.datetime.today()
		self.transacoes = []

	def imprimir(self):
		print(f"Data de abertura: {self.data_abertura}")
		print("Transações: ")
		for transacao in self.transacoes:
			print("-", transacao)

class Funcionario(abc.ABC):

	def __init__(self, nome, cpf, salario):
		self._nome = nome
		self._cpf = cpf
		self._salario = salario

	@abc.abstractmethod
	def get_bonificacao(self):
		pass

class Gerente(Funcionario, AutenticacaoMixIn, HoraExtraMixIn):

	def __init__(self, nome, cpf, salario, senha, qtd_gerenciaveis):
		super().__init__(nome, cpf, salario)
		self._senha = senha
		self._qtd_gerenciaveis = qtd_gerenciaveis

	def autenticacao(self, senha):
		if self.senha == senha:
			print("Acesso permitido.")
			return True
		else:
			print("Acesso negado.")
			return True

	def get_bonificacao(self):
		return self._salario * 0.15

class Diretor(Funcionario, AutenticacaoMixIn):

	def __init__(self, nome, cpf, salario):
		super().__init__(nome, cpf, salario)

	def get_bonificacao(self):
		return self._salario * 0.20

class Escriturario(Funcionario, AtendimentoMixIn):
	pass

class ControleDeBonificacoes:

	def __init__(self, total_bonificacoes=0):
		self._total_bonificacoes = total_bonificacoes

	def registrar(self, obj):
		if hasattr(obj, "get_bonificacao"):
			self._total_bonificacoes += obj.get_bonificacao()
		else:
			print(f"A instância de {obj.__class__.__name__} não implementa o método get_bonificacao().")

	@property
	def total_bonificacoes(self):
		return self._total_bonificacoes

# some tests of the written code above:

# cliente_um = Cliente('João', 'Oliveira', '11111111111-11')
# cliente_dois = Cliente('José', 'Azevedo', '222222222-22')
# conta_um = Conta('123-4', cliente_um, 1000.0)
# conta_dois = Conta('123-5', cliente_dois, 1000.0)
# conta_um.depositar(100.0)
# conta_um.sacar(50.0)
# conta_um.transferir(conta_dois, 200.0)
# conta_um.extrato()
# conta_um.historico.imprimir()
# conta_dois.historico.imprimir()
# criar_cliente_um = Cliente('John', 'Nada', '333333333-33')
# criar_cliente_dois = Cliente('Jane', 'Doe', '444444444-44')
# criar_conta_um = Conta('123-6', criar_cliente_um, 1000.0)
# criar_conta_dois = Conta('123-7', criar_cliente_dois, 1000.0)
# print(f"Total de contas: {Conta.get_total_contas()}")
# print("*" * 50)
# gerente = Gerente('José', '222222222-22', 5000.0, '1234', 0)
# print(gerente.get_bonificacao())
# print("*" * 50)
# if __name__ == '__main__':
	# funcionario = Funcionario("João", "111111111-11", 2000.0)
	# print(f"Bonificação do funcionário: {funcionario.get_bonificacao()}")

	# gerente = Gerente("José", "222222222-22", 5000.0, "1234", 0)
	# print(f"Bonificação do gerente: {gerente.get_bonificacao()}")

	# controle = ControleDeBonificacoes()
	# controle.registrar(funcionario)
	# controle.registrar(gerente)

	# print(f"Total: {controle.total_bonificacoes}")

	# cliente = Cliente("Maria", "333333333-33", "1234")
	# controle = ControleDeBonificacoes()
	# controle.registrar(cliente)

# if __name__ == '__main__':
	# conta = Conta("123-4", "João", 1000.0)
	# conta_corrente = ContaCorrente("123-5", "José", 1000.0)
	# conta_poupanca = ContaPoupanca("123-6", "Maria", 1000.0)

	# conta.definir_tipo_taxa(0.01)
	# conta_corrente.definir_tipo_taxa(0.01)
	# conta_poupanca.definir_tipo_taxa(0.01)

	# print(conta._saldo)
	# print(conta_corrente._saldo)
	# print(conta_poupanca._saldo)

# if __name__ == '__main__':
	# gerente = Gerente("José", "222222222-22", 5000.0, "1234", 0)
	# print(gerente.get_bonificacao())
	# diretor = Diretor("João", "111111111-11", 4000.0)
	# print(diretor.get_bonificacao())

# if __name__ == '__main__':
	# conta = Conta()
	# conta_investimento = ContaInvestimento("123-6", "Maria", 1000.0)
	# conta_investimento.depositar(1000.0)
	# conta_investimento.definir_tipo_taxa(0.01)
	# print(conta_investimento.__class__.__name__)
	# print(conta_investimento._saldo)

# if __name__ == '__main__':
	# diretor = Diretor("João", "111111111-11", 3000.0)
	# gerente = Gerente("José", "222222222-22", 5000.0, "1235", 0)
	# cliente = Cliente("Maria", "333333333-33", "1236")

	# sistema = SistemaInterno()
	# sistema.login(diretor)
	# sistema.login(gerente)
	# sistema.login(cliente)

if __name__ == '__main__':

	conta_corrente_um = ContaCorrente("123-4", "João", 1000.0)
	conta_corrente_dois = ContaCorrente("123-4", "José", 1000.0)
	seguro_um = SeguroDeVida(100.0, "José", "345-77")
	seguro_dois = SeguroDeVida(200.0, "Maria", "237-98")

	lista_tributaveis = []
	lista_tributaveis.append(conta_corrente_um)
	lista_tributaveis.append(conta_corrente_dois)
	lista_tributaveis.append(seguro_um)
	lista_tributaveis.append(seguro_dois)

	manipulador = ManipuladorDeTributaveis()
	total = manipulador.calcular_impostos(lista_tributaveis)

	print(total)


