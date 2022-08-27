#!/usr/bin/env node

// using literal notation
const objectOne = {}
console.log(objectOne)

// object in JS
console.log(typeof Object, typeof new Object)
const objectTwo = new Object
console.log(objectTwo)

// constructors functions
function Product(name, price, disc) {
	this.name = name
	this.getPriceWithDiscount = () => price * (1 - disc)
}

const productOne = new Product("Notebook", 2458.99, 0.30)
const productTwo = new Product("Book", 35.45, 0.15)

console.log(productOne.getPriceWithDiscount().toFixed(2))
console.log(productTwo.getPriceWithDiscount().toFixed(2))

// factory function
function createWorker(name, salary, absences) {
	return {
		name,
		salary,
		absences,
		getSalary(){
			return (salary / 30) * (30 - absences)
		}
	}
}

const workerOne = createWorker("John Nada", 6500, 3)
const workerTwo = createWorker("Jane Doe", 7500, 2)

console.log(workerOne.getSalary().toFixed(2))
console.log(workerTwo.getSalary().toFixed(2))

// object.create
const daughter = Object.create(null)
daughter.name = "Jane Doe"
console.log(daughter)

// JSON function that returns a object
const fromJSON = JSON.parse('{"name": "The Nothing"}')
console.log(fromJSON.name)
