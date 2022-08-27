#!/usr/bin/env node

const value = "Global"

function out() {
	const value = "Local"
	function inside () {
		return value
	}
	return inside
}

const myFunction = out()
console.log(myFunction())
