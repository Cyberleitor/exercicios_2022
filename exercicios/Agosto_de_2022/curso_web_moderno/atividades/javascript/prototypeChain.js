#!/usr/bin/env node

const grandfather = { attrOne: "A"}
const father = {__proto__: grandfather, attrTwo: "B"}
const son = {__proto__: father, attrThree: "C"}
console.log(son.attrOne, son.attrTwo, son.attrThree)

const car = {
	currentSpeed: 0,
	maxSpeed: 200,
	accelerate(delta) {
		if (this.currentSpeed + delta <= this.maxSpeed) {
			this.currentSpeed += delta
		} else {
			this.currentSpeed = this.maxSpeed
		}
	},
	status() {
		return `${this.currentSpeed}Km/h de ${this.maxSpeed}Km/h`
	}
}

const ferrari = {
	model: "F40",
	maxSpeed: 320
}

const volvo = {
	model: "V40",
	status() {
		return `${this.model}: ${super.status()}`
	}
}

Object.setPrototypeOf(ferrari, car)
Object.setPrototypeOf(volvo, car)

console.log(ferrari)

volvo.accelerate(120)
console.log(volvo.status())
