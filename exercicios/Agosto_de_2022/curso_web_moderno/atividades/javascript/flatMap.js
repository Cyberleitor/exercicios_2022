#!/usr/bin/env node

const school = [{
	name: "Turma A1",
	students: [{
		name: "John Nada",
		grade: 8.5
	}, {
		name: "Jane Doe",
		grade: 9.7
	}]
}, {
	name: "Turma A2",
	students: [{
		name: "Juan Nothing",
		grade: 8.75
	}, {
		name: "June Never",
		grade: 9.85
	}]
}]

const getStudentsGrade = student => student.grade
const getGradesOfGroup = group => group.students.map(getStudentsGrade)

const firstGrade = school.map(getGradesOfGroup)
console.log(firstGrade)

Array.prototype.flatMap = function(callback) {
	return Array.prototype.concat.apply([], this.map(callback))
}

const secondGrade = school.flatMap(getGradesOfGroup)
console.log(secondGrade)
