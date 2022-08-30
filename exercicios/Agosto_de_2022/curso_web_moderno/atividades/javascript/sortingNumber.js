#!/usr/bin/env node

function pickingNumber(numberChosen) {
	randomNumber = Math.floor(Math.random() * (10 - 1 + 1) + 1)
	if (numberChosen === randomNumber) {
		console.log(`Parabéns! O número sorteado foi o ${numberChosen}.`)
	} else {
		console.log(`Que pena! O número sorteado foi o ${randomNumber}.`)
	}
}

pickingNumber(9)
pickingNumber(4)
