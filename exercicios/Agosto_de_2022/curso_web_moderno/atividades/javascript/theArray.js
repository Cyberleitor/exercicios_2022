#!/usr/bin/env node

let approved = new Array("Beatriz", "Carlos", "Ana")
console.log(approved)

approved = ["Beatriz", "Carlos", "Ana"]
console.log(approved[0])
console.log(approved[2])

approved[3] = "Paulo"
approved.push("Cassandra")
console.log(approved.length)
console.log(approved)

approved.sort()
console.log(approved)

approved.splice(2, 0, "M-ly", "Beth")
console.log(approved)
