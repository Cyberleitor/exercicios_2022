#!/usr/bin/env node

firstArray = [23, 14, 62, 42, 23]
secondArray = [25, 19, 47, 72, 93]

let sumNumbers = arrayNumbers => console.log(arrayNumbers.reduce((accumulator, currentNumber) => accumulator + currentNumber, 0))

sumNumbers(firstArray)
sumNumbers(secondArray)
