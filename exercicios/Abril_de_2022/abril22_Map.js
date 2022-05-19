const maca = {
    value: 7,
}

const laranja = {
    value: 12,
}

function mapComThis(arr, thisArg){
    return arr.map(function(item) {
       return item * this.value;
    }, thisArg);
}

const nums = [3];

console.log('this -> Maça', mapComThis(nums, maca));

console.log('this -> Laranja', mapComThis(nums, laranja));