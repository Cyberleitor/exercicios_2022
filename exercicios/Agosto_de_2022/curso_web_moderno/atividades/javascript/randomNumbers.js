#!/usr/bin/env node

function rand({ min = 1, max = 1000 } = {}) {
	const valor = Math.random() * (max - min) + min
	return Math.floor(valor)
}

const number = { max: 20, min: 1 }
console.log(rand(number))
