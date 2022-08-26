#!/usr/bin/env node

const informarResultado = function (nota) {
	switch (Math.floor(nota)) {
		case 10:
			console.log("Aprovado com extrema honra!")
			break
		case 9:
			console.log("Aprovado com honra!")
			break
		case 8:
			console.log("Aprovado.")
			break
		case 7:
			console.log("Aprovado.")
			break
		case 6:
			console.log("Reprovado.")
			break
	}
}

informarResultado(10)
informarResultado(9.5)
informarResultado(6.5)
