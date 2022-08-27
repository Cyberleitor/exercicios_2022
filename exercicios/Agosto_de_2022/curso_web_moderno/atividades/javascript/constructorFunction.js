#!/usr/bin/env node

function Car(maxSpeed = 200, delta = 5) {
	let currentSpeed = 0
	this.accelerate = function() {
		if (currentSpeed + delta <= maxSpeed) {
			currentSpeed += delta
		} else {
			currentSpeed = maxSpeed
		}
	}
	this.getCurrentSpeed = () => currentSpeed
}

const impala = new Car
impala.accelerate()
impala.accelerate()
impala.accelerate()
console.log(impala.getCurrentSpeed())

