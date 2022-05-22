import numpy as np

class VetorOrdenado:

    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = np.empty(self.capacidade, dtype=int)

    def imprimir(self):
        if self.ultima_posicao == -1:
            print('O vetor está vazio.')
        else:
            for i in range(self.ultima_posicao + 1):
                print(f'{i} - {self.valores[i]} ')

    def inserir(self, valor):
        if self.ultima_posicao == self.capacidade - 1:
            print('Capacidade máxima atingida.')
            return

        posicao = 0
        for i in range(self.ultima_posicao + 1):
            posicao = i
            if self.valores[i] > valor:
                break
            if i == self.ultima_posicao:
                posicao = i + 1

        posicao_final = self.ultima_posicao
        while posicao_final >= posicao:
            self.valores[posicao_final + 1] = self.valores[posicao_final]
            posicao_final -= 1

        self.valores[posicao] = valor
        self.ultima_posicao += 1

print('Qual é o tamanho do vetor a ser criado? ')
resposta_vetor = int(input())
vetor = VetorOrdenado(resposta_vetor)

indice = 1

while indice <= resposta_vetor:
    print(f'Qual é o {indice}º a ser inserido no vetor? ')
    resposta_item = int(input())
    vetor.inserir(resposta_item)
    indice += 1

vetor.imprimir()
