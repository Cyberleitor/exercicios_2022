function filtraPares(arr) {
    return arr.filter(callback);
}

function callback(item) {
    return item % 2 === 0;
}

const meuArray = [3, 6, 22,  9, 7, 11, 34];

console.log(filtraPares(meuArray));