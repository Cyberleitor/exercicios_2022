#!/usr/bin/env node

expendituresOne = [{name: "Computer", category: "Hardware", price: 3550},
		{name: "Cinema", category: "Entertainment", price: 50}]

expendituresTwo = [{name: "Books", category: "Studies", price: 225},
		{name: "Food", category: "Necessary things", price: 2380}]

let totalBudget = shopping => console.log(shopping.reduce((accumulator, currentValue) => accumulator + currentValue.price, 0))

totalBudget(expendituresOne)
totalBudget(expendituresTwo)
