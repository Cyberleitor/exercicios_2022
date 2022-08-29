#!/usr/bin/env node

function reversalReturn(value) {
	const type = typeof value

	if (type == "boolean") return !value
	else if (type == "number") return -value
	else
		return `Boolean or number is waited, but the parameter is of the ${type} type.`
}

console.log(reversalReturn(true))
console.log(reversalReturn(false))
console.log(reversalReturn(42))
console.log(reversalReturn(-27))
console.log(reversalReturn("Testing"))
