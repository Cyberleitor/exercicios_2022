#!/usr/bin/env node

firstPhrase = "Is this the real life?"
secondPhrase = "Is this just a phantasy?"
thirdPhrase = "No scape from reality."

function countingLetter(searchedLetter, thePhrase) {
	console.log([...thePhrase].filter(letter => letter === searchedLetter).length)
}

countingLetter("s", firstPhrase)
countingLetter("s", secondPhrase)
countingLetter("s", thirdPhrase)
