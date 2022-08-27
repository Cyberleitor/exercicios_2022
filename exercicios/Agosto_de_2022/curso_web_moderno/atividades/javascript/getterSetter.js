#!/usr/bin/env node

const sequence = {
	_value: 1,
	get value() { return this._value++ },
	set value(value) {
		if (value > this._value) {
			this._value = value
		}
	}
}

console.log(`${sequence.value} | ${sequence.value}`)
