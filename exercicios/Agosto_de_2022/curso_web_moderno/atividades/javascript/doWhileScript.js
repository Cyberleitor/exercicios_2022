#!/usr/bin/env node

function pegarInteiroAleatorio (min, max) {
	const valor = Math.random() * (max - min) + min
	return Math.floor(valor)
}

let opcao

do {
	opcao = pegarInteiroAleatorio(-1, 10)
	console.log(`O número sorteado foi ${opcao}.`)
} while (opcao != -1) 

console.log("O sorteio terminou.")
