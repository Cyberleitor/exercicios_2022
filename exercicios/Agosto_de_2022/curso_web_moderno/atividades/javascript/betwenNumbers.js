#!/usr/bin/env node

betwenNumbers = (minimum, maximum, number, inclusive = false) => inclusive ? number >= minimum && number <= maximum : number > minimum && number < maximum

console.log(betwenNumbers(2, 10, 7))
console.log(betwenNumbers(2, 10, 11))
