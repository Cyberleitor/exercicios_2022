from abc import ABCMeta, abstractmethod

print('Informe o título do livro: ')
title = input()
print('Informe o autor do livro: ')
author = input()
print('Informe o valor do livro: ')
price = int(input())

class Book(object, metaclass=ABCMeta):
    def __init__(self, title, author):
        self.title = title
        self.author = author
    @abstractmethod
    def display(): pass

class MyBook(Book):
    def __init__(self, title, author, price):
        Book.__init__(self, title, author)
        self.price = price
    def display(self):
        print(f'Title: {self.title}\nAuthor: {self.author}\nPrice: {self.price}')

new_novel = MyBook(title, author, price)
new_novel.display()