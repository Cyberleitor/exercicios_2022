#!/usr/bin/env node

const person = {
	name: "John Nada",
	age: 33,
	presentation() {
		console.log(`Hello, I'm ${this.name} and I'm ${this.age} years old!`)
	}
}

person.presentation()
