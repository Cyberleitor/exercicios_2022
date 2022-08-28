#!/usr/bin/env node

const product = Object.preventExtensions({
	name: "Anything", price: 4.25, tag: "Promotion"
})

console.log("Is this extensible? ", Object.isExtensible(product))

product.name = "Borracha"
delete product.tag
console.log(product)

const person = Object.seal({
	name: "Jane Doe", age: 42
})
console.log("Is the object sealed? ", Object.isSealed(person))

person.age = 35
console.log(person)
