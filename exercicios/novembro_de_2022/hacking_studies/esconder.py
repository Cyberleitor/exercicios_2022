#!/usr/bin/python3

photo = input("Em qual foto deseja ocultar o programa? ")
program = input("Qual é o programa que deseja ocultar? ")
with open(f"{photo}", "ab") as image, open(f"{program}", "rb") as binary:
	image.write(binary.read())
