#!/usr/bin/env node

firstObject = {
	name: "John Nada",
	profession: "Hacker"
}

secondObject = {
	name: "Jane Doe",
	profession: "Programmer"
}

let objectToArray = object => console.log(Object.entries(object))

objectToArray(firstObject)
objectToArray(secondObject)
