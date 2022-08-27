#!/usr/bin/env node

const person = {
	name: "Jane Doe",
	age: 33,
	hobby: "Programming"
}

console.log(Object.keys(person))
console.log(Object.values(person))
console.log(Object.entries(person))

Object.defineProperty(person, "birthday", {
	enumerable: true,
	writable: false,
	value: "19/6/1994"
})

Object.entries(person).forEach(([key, value]) => {
	console.log(`${key}: ${value}`)
})
