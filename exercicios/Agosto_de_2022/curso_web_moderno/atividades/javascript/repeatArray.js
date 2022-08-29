#!/usr/bin/env node

function repeatArray(element, multiplicator) {
	theArray = []
	while (multiplicator > 0) {
		theArray.push(element)
		multiplicator--
	}
	console.log(theArray)
}

repeatArray(7, 10)
repeatArray(4, 3)
repeatArray("John Nada", 6)
