#!/usr/bin/env node

const superMarketBasket = [
	'{ "product": "Borracha", "price": 3.45 }',
	'{ "product": "Caderno", "price": 13.90 }',
	'{ "product": "Kit de Lápis", "price": 41.22 }',
	'{ "product": "Caneta", "price": 7.50}'
]

const toObject = json => JSON.parse(json)
const onlyPrice = item => item.price

const arrayWithPrices = superMarketBasket.map(toObject).map(onlyPrice)
console.log(arrayWithPrices)
