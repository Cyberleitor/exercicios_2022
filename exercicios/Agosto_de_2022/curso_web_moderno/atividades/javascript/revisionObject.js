#!/usr/bin/env node

const produto = new Object
produto.nome = "Cadeira"
produto["marca do produto"] = "Genérica"
produto.preco = 220

console.log(produto)

const car = {
	model: "Ferrari",
	value: 2500999,
	owner: {
		name: "John Nada",
		age: 33,
		address: {
			street: "Heaven",
			number: "666",
			city: "Hell"
		}
	}
}

console.log(car)
console.log(`O proprietário desse carro é ${car.owner.name}.`)
