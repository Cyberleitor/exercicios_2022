#!/usr/bin/env node

arrayOfWords = ["Programador", "Aprovar", "Avaliação", "Notificação", "Orientado"]

let filteringLettersInWords = (letters, theArray) => console.log(theArray.filter(letter => letter.includes(letters)))

filteringLettersInWords("pro", arrayOfWords)
filteringLettersInWords("va", arrayOfWords)
filteringLettersInWords("do", arrayOfWords)
