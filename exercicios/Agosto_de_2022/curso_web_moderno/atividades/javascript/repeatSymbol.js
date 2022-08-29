#!/usr/bin/env node

function repeatSymbol(multiplicator) {
	let result = ""
	for (let index = 0; index < multiplicator; index++)
		result += "+"
	console.log(result)
}

repeatSymbol(4)
repeatSymbol(6)
repeatSymbol(2)
repeatSymbol(10)
