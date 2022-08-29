#!/usr/bin/env node

randomArrayOne = ["JavaScript", 19, "Python", 42]
randomArrayTwo = [23, 78, "Jane Doe", "John Nada", 52]

let filteringNumbers = theArray => console.log(theArray.filter(index => typeof index === "number"))

filteringNumbers(randomArrayOne)
filteringNumbers(randomArrayTwo)
