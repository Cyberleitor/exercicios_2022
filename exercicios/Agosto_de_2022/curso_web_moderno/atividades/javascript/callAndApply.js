#!/usr/bin/env node

function getPrice(tax = 0, money = "R$") {
	return `${money} ${this.price * (1 - this.disc) * (1 + tax)}`
}

const car = {price: 50456, disc: 0.35}

console.log(getPrice.call(car))
console.log(getPrice.apply(car))

console.log(getPrice.call(car, 0.15, "$"))
console.log(getPrice.apply(car, [0.15, "$"]))
