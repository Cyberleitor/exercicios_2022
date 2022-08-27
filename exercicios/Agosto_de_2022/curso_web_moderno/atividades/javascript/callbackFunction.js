#!/usr/bin/env node

const industries = ["Mercedes", "Audi", "BMW"]

function printIndustries(name, index) {
	console.log(`${index + 1}. ${name}`)
}

industries.forEach(printIndustries)
industries.forEach(industries => console.log(industries))
