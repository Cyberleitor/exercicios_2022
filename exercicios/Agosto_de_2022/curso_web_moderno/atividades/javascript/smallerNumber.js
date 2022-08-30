#!/usr/bin/env node

firstArray = [19, 47, 32, 45, 68, 6, 12, 9]
secondArray = [23, 15, 13, 105, 27, 9, 10, 12]

function smallNumber(arrayOfNumbers) {
	theSmallestNumber = arrayOfNumbers[0]
	for (index = 0; index < arrayOfNumbers.length; index++) {
		if (theSmallestNumber > arrayOfNumbers[index]) {
			theSmallestNumber = arrayOfNumbers[index]
		} else {
			theSmallestNumber = theSmallestNumber
		}
	}
	console.log(theSmallestNumber)
}

smallNumber(firstArray)
smallNumber(secondArray)
