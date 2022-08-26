#!/usr/bin/env node

function avaliarNota(nota) {
	if (nota >= 7) {
		console.log(`Aprovado com ${nota}!`)
	} else {
		console.log(`Infelizmente, ${nota} não está acima da média.`)
	}
}

avaliarNota(8.5)
avaliarNota(6.9)
