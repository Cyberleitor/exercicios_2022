#!/usr/bin/env node

Array.prototype.forEachTest = function(callback) {
	for (let index = 0; index < this.length; index++) {
		callback(this[index], index, this)
	}
}

const approved = ["Jane Doe", "John Nada", "Summer", "Leon", "Alien"]

approved.forEachTest((name, index) => console.log(`${index + 1}. ${name}`))
