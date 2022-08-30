#!/usr/bin/env node

firstString = "This is a test"
secondString = "This is a test too, but more long"
thirdString = "This is a test too, but more long because I need make some tests"

let countingWords = theString => console.log((numberOfWords = theString.split(" ")).length)

countingWords(firstString)
countingWords(secondString)
countingWords(thirdString)
