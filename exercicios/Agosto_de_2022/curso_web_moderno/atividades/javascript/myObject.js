#!/usr/bin/env node

function myObject() {}

const objectOne = new myObject
const objectTwo = new myObject

myObject.prototype.name = "Anônimo"
myObject.prototype.talk = function() {
	console.log(`Olá, meu nome é ${this.name}!`)
}

objectOne.talk()

objectTwo.name = "John Nada"
objectTwo.talk()
