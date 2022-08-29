#!/usr/bin/env node

let firstArray = ["John Nada", "Jane Doe", "Summer Eletrohits", "Leon Hyll", "Lycan", "Sandes"]
let secondArray = [20, 32, 27, 19, 36]
let thirdArray = ["Lycan", 666, "Aliem", 42, 23, "Márcio", 78]

function makeNewArray(theArray) {
	const firstIndex = theArray.shift()
	const lastIndex = theArray.pop()

	console.log([firstIndex, lastIndex])
}

makeNewArray(firstArray)
makeNewArray(secondArray)
makeNewArray(thirdArray)

console.log(firstArray)
console.log(secondArray)
console.log(thirdArray)
