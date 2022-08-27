#!/usr/bin/env node

const notes = [7.7, 6.5, 5.2, 8.9, 3.6, 7.1, 9.0]

const lowNotes = notes.filter(note => note < 7)

console.log(lowNotes)
console.log(notes) // only to show that the original array doesn't was modified.
