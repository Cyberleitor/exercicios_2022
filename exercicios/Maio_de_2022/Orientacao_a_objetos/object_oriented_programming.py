'''Crie uma classe chamada aluno com os seguintes atributos:
– Nome
– Nota 1
– Nota 2
– Crie um construtor para a classe (__init__)
Crie as seguintes funções (métodos):
– Calcula média, retornando a média aritmética entre as notas
– Mostra dados, que somente imprime o valor de todos os atributos
– Resultado, que verifica se o aluno está aprovado ou reprovado (se a média for maior ou igual a 6.0, o aluno está aprovado)
Crie dois objetos (aluno1 e aluno2) e teste as funções'''

class Student:
    def __init__(self, name, score_one, score_two):
        self.name = name
        self.score_one = score_one
        self.score_two = score_two
    def calculating_averaging(self):
        return f'Média {(self.score_one + self.score_two) / 2}.'
    def show_values(self):
        return f'{self.name}: {self.score_one}, {self.score_two}.'
    def approved_or_reproved(self):
        if (self.score_one + self.score_two) / 2 >= 6:
            return f'{self.name} obteve aprovação.'
        else:
            (self.score_one + self.score_two) / 2 < 6
            return f'{self.name} não obteve aprovação.'

student_one = Student('John Nada', 7.0, 4.0)
student_two = Student('Jane Doe', 9.0, 8.0)

print(f'{student_one.show_values()} {student_one.calculating_averaging()} {student_one.approved_or_reproved()}')
print(f'{student_two.show_values()} {student_two.calculating_averaging()} {student_two.approved_or_reproved()}')