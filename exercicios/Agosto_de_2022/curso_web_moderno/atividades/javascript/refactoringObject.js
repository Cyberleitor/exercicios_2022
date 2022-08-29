#!/usr/bin/env node

students = {name: ["John Nada", "Jane Doe", "Summer Eletrohits"], group: ["A19", "B42", "C13"], evaluation: [10, 8, 10]}

function refactoringObject(object, propertyToRemove) {
	const refactoredObject = Object.assign({}, object)
	delete refactoredObject[propertyToRemove]

	console.log(refactoredObject)
}

refactoringObject(students, "group")
