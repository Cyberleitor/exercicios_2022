#!/usr/bin/env node

firstWord = "Reality"
secondWord = "Nothing"
thirdWord = "Infinity"

let removingVowels = theWord => console.log(theWord.replace(/[aeiou]/ig, ""))

removingVowels(firstWord)
removingVowels(secondWord)
removingVowels(thirdWord)
