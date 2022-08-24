#!/usr/bin/env node

var firstValue = 7;
var secondValue = 94;

[firstValue, secondValue] = [secondValue, firstValue];

console.log(`${firstValue}`);
console.log(`${secondValue}`);
