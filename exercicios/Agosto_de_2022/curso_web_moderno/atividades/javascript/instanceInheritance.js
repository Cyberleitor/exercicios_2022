#!/usr/bin/env node

function Class(name, videoID) {
	this.name = name
	this.videoID = videoID
}

function newer(func, ...params) {
	const object = {}
	object.__proto__ = func.prototype
	func.apply(object, params)
	return object
}

const classOne = newer(Class, "Hacking", 999)
const classTwo = newer(Class, "Cloud Computing", 4242)

console.log(classOne)
console.log(classTwo)
