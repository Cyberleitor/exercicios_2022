#!/usr/bin/env node

const numbers = [1, 2, 3, 4, 5]

let result = numbers.map((element) => element * 2)
console.log(result)

const sumTen = element => element + 10
const tripleValue = element => element * 3
const toMoney = element => `R${parseFloat(element).toFixed(2).replace('.', ',')}`

result = numbers.map(sumTen).map(tripleValue).map(toMoney)
console.log(result)
