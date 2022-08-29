#!/usr/bin/env node

function checkingLeapYear(year) {
	const divisionByFour = year % 4 == 0
	const divisionByHundred = year % 100 == 0
	const divisionByFourHundred = year % 400 == 0

	console.log((divisionByFour && !divisionByHundred) || divisionByFourHundred)
}

checkingLeapYear(2020)
checkingLeapYear(2100)
checkingLeapYear(2088)
