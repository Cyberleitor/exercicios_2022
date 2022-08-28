#!/usr/bin/env node

const object = { a: 4, b: 2, c: 3, sum() { return object.a + object.b + object.c } }
console.log(object.sum())

archiveJson = JSON.stringify(object)
console.log(archiveJson)

archiveObject = JSON.parse(archiveJson)
console.log(archiveObject)
