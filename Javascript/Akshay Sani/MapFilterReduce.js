const arr = [5, 1, 3, 2, 6]

let output = []

function double(el) {
    return el * 2
}
function triple(el) {
    return el * 3
}
function binary(el) {
    return el.toString(2)
}

output = arr.map(double)
console.log(output)

output = arr.map(triple)
console.log(output)

output = arr.map(binary)
console.log(output)

function odd(el) {
    return el % 2
}

function even(el) {
    return el % 2 === 0
}

output = arr.filter(odd)
console.log(output)

output = arr.filter(even)
console.log(output)

let max = -1;
let sum = 0;
function sumOrMax(arr) {
    for(let i = 0; i < arr.length; i++){
        if(arr[i] > max){
            max = arr[i]
        }
        sum += arr[i]
    }
    console.log(sum)
    console.log(max)
}
sumOrMax(arr)

let maxi = arr.reduce(function (acc, current) {
    acc = Math.max(acc,current)
    return acc
}, -1)
console.log(maxi)

let summ = arr.reduce(function sum(acc, curr){
    acc = acc + curr
    return acc
}, 0)
console.log(summ)

const arr2 = [
    {first: 'Fahim1', last: 'Fahad', age: 26},
    {first: 'Fahim2', last: 'Fahad', age: 75},
    {first: 'Fahim3', last: 'Fahad', age: 32},
    {first: 'Fahim4', last: 'Fahad', age: 50},
    {first: 'Fahim5', last: 'Fahad', age: 29},
    {first: 'Fahim6', last: 'Fahad', age: 26},
]

let arr3 = [1, 1, 1, 1, 1, 2, 3, 3, 3, 3, 5, 5, 6, 7, 8, 9, 9, 9, 9]
let prev = null
let output2 = []
function checkDuplicate(el){
    if(el !== prev){
        prev = el
        output2.push(el)
    }
}
arr3.map(checkDuplicate)
console.log(output2)

let person = arr2.reduce(function (final, curr) {
    if(final[curr.age]){
        final[curr.age] += 1
    } else{
        final[curr.age] = 1
    }
    return final
}, {})

console.log(person)