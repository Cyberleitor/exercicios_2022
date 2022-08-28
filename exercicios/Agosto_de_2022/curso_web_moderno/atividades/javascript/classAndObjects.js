#!/usr/bin/env node

class financialControl {
	constructor(name = "Anything", value = 0) {
		this.name = name
		this.value = value
	}
}

class financialPlan {
	constructor(month, year) {
		this.month = month
		this.year = year
		this.expenditures = []
	}
	addExpenditures(...expenditures) {
		expenditures.forEach(expend => this.expenditures.push(expend))
	}
	summary() {
		let totalValue = 0
		this.expenditures.forEach(expend => {
			totalValue += expend.value
		})
		return totalValue
	}
}

const salary = new financialControl("Salary", 45699)
const lightBill = new financialControl("Light's bill", -165)
const foodForMonth = new financialControl("Food", -2500)
const internetBill = new financialControl("Internet", -110)
const waterBill = new financialControl("Water", -150)
const gasBill = new financialControl("Gas", -200)

const bills = new financialPlan(8, 2022)
bills.addExpenditures(salary, lightBill, foodForMonth, internetBill, waterBill, gasBill)
console.log(bills.summary())
