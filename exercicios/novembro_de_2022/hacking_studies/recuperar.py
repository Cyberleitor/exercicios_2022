#!/usr/bin/python3

photo = input("De qual imagem deseja extrair o programa oculto? ")

with open(f"{photo}", "rb") as image:
	program = image.read()
	deslocamento = program.index(bytes.fromhex("FFD9"))

	image.seek(deslocamento + 2)

	with open("the_program", "wb") as the_program:
		the_program.write(image.read())
