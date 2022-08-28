#!/usr/bin/env node

const products = [
	{ name: "Notebook", price: 2499, fragile: true },
	{ name: "iPad Pro", price: 4199, fragile: true },
	{ name: "Glass cup", price: 14.85, fragile: true},
	{ name: "Platic cup", price: 10.49, fragile: false}
]

const itIsExpensive = product => product.price >= 500
const itIsFragile = product => product.fragile

console.log(products.filter(itIsExpensive).filter(itIsFragile))
