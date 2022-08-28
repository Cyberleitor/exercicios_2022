#!/usr/bin/env node

const students = [
	{ name: "John Nada", grade: 7.3, scholar: false },
	{ name: "Jane Doe", grade: 9.5, scholar: true },
	{ name: "Peter Nothing", grade: 6.8, scholar: false },
	{ name: "Agatha Diamond", grade: 8.7, scholar: true }
]

const allStudentsAreScholar = (result, scholar) => result && scholar
console.log(students.map(student => student.scholar).reduce(allStudentsAreScholar))

const someScholar = (result, scholar) => result || scholar
console.log(students.map(student => student.scholar).reduce(someScholar))
