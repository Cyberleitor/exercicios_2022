#!/usr/bin/env node

const father = { name: "John Nada", colorHair: "black" }

const daughterOne = Object.create(father)
daughterOne.name = "Jane Doe"
console.log(`${daughterOne.name} has ${daughterOne.colorHair} hair.`)

const daughterTwo = Object.create(father, {
	name: { value: "Jane Nada", writable: false, enumerable: true },
	skin: { value: "golden", writable: false, enumerable: true }
})

console.log(`${daughterTwo.name} has ${daughterTwo.colorHair} hair and ${daughterTwo.skin} skin.`)

for (let key in daughterTwo) {
	daughterTwo.hasOwnProperty(key) ?
		console.log (key) : console.log(`Por herança: ${key}.`)
}
