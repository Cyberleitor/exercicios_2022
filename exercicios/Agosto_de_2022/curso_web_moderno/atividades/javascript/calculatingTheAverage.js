#!/usr/bin/env node

arrayOfGradesOne = [7.5, 10, 8.25, 6.85]
arrayOfGradesTwo = [9, 7.25, 6.5, 8]

function calculatingTheAverage(arrayOfGrades) {
	const arrayLength = arrayOfGrades.length
	const totalGrade = arrayOfGrades.reduce((accumulator, currentValue) => accumulator + currentValue)
	console.log((totalGrade / arrayLength).toFixed(2))
}

calculatingTheAverage(arrayOfGradesOne)
calculatingTheAverage(arrayOfGradesTwo)
