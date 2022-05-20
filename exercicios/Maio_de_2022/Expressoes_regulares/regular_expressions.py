import re

texto_um = 'O meu e-mail é blablabla@gmail.com, tenho o CPF 000000000-00 e resido no CEP 33333-333.'
texto_dois = 'O meu e-mail é blebleble@outlook.com, tenho o CPF 111111111-11 e resido no CEP 44444-445.'
texto_tres = 'O meu e-mail é blublublu@microsoft.com, tenho o CPF 222222222-22 e resido no CEP 55555-555.'

print(re.findall('\w+@\w+\.\w{3}', texto_um))
print(re.findall('\w+@\w+\.\w{3}', texto_dois))
print(re.findall('\w+@\w+\.\w{3}', texto_tres))

print(re.findall('\d{9}-\d{2}', texto_um))
print(re.findall('\d{9}-\d{2}', texto_dois))
print(re.findall('\d{9}-\d{2}', texto_tres))

print(re.findall('\d{5}-\d{3}', texto_um))
print(re.findall('\d{5}-\d{3}', texto_dois))
print(re.findall('\d{5}-\d{3}', texto_tres))

'''Com as linhas de código abaixo, pretendia abrir um arquivo em um repositório local e extrair dele
as seguintes informações: nome, e-mail e número de telefone, não necessariamente nessa ordem, a fim de vislumbrar
a aplicabilidade das expressões regulares.'''

with open(r'C:\<PATH_TO_LOCAL_ARCHIVE>', encoding='utf8') as bloco:
    for linha in bloco:
        print(re.findall('\w+@\w+\.\w{3}', linha))
        print(re.findall('[A-Z]\w+\s\w+', linha))
        print(re.findall('\(\d{2}\)\s\d+\.\d{4}', linha))