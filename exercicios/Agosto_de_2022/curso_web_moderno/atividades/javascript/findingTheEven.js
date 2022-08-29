#!/usr/bin/env node

firstArray = [19, 42, 23, 36, 82, 93, 16, 43, 28]
secondArray = [64, 89, 75, 37, 49, 52, 85, 74, 92]

function findingTheEven(theArray) {
	arrayWithEvens = []
	for (index = 0; index < theArray.length; index += 2) {
		if (theArray[index] % 2 == 0)
			arrayWithEvens.push(theArray[index])
	}
	console.log(arrayWithEvens)
}

findingTheEven(firstArray)
findingTheEven(secondArray)
