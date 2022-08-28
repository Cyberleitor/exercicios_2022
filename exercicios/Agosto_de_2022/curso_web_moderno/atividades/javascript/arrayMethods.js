#!/usr/bin/env node

const drivers = ["Adam", "Livia", "Cassie", "Mary", "Leonard"]
console.log(drivers)

drivers.pop()
console.log(drivers)

drivers.push("Sophie")
console.log(drivers)

drivers.shift()
console.log(drivers)

drivers.unshift("Summer")
console.log(drivers)

const otherGroupOfDrivers = drivers.slice(0, 4)
console.log(otherGroupOfDrivers)
console.log(drivers)
