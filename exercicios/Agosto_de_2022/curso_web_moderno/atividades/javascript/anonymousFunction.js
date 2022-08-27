#!/usr/bin/env node

const sum = (firstValue, secondValue) => firstValue + secondValue

const printResult = (firstNumber, secondNumber, makeMath = sum) => console.log(makeMath(firstNumber, secondNumber))

printResult(27, 4)
printResult(9, 5)
printResult(13, 3, function (firstValue, secondValue) {
	return firstValue - secondValue
})
printResult(8, 5, (firstValue, secondValue) => firstValue * secondValue)
