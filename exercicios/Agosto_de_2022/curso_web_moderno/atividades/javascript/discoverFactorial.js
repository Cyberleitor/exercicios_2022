#!/usr/bin/env node

function discoverFactorial(number) {
	return number ? number * discoverFactorial(number - 1) : 1
}

console.log(discoverFactorial(5))
console.log(discoverFactorial(14))
console.log(discoverFactorial(20))
