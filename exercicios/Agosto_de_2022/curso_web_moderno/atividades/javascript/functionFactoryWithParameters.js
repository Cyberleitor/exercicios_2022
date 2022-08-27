#!/usr/bin/env node

function createProduct(name, price) {
	return {
		name,
		price
	}
}

console.log(createProduct("CPU", 1000))
