#!/usr/bin/env node

const students = [
	{ name: "John Nada", grade: 7.5 },
	{ name: "Jane Doe", grade: 9.75 }
]

// Imperative
let totalGradeOne = 0
for (let index = 0; index < students.length; index++) {
	totalGradeOne += students[index].grade
}
console.log((totalGradeOne / students.length).toFixed(2))

// Declarative
const getGrade = student => student.grade
const sum = (total, current) => total + current
const totalGradeTwo = students.map(getGrade).reduce(sum)
console.log((totalGradeTwo / students.length).toFixed(2))
