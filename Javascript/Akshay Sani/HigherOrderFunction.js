function x() {
    console.log("X")
}

function y(cb) {
    cb()
}

y(x)

const calculateCircle = (radiusArray, callbackCalculate) => {
    let output = []
    radiusArray.map((radius) => output.push(callbackCalculate(radius)))
    return output
}
const area = (rad) => {
    return Math.PI * rad * rad
}
const circumference = (rad) => {
    return 2 * Math.PI * rad
}
const diameter = (rad) => {
    return 2 * rad
}

const radius = [3, 2, 4, 1]

console.log(radius.map(area))
console.log(radius.map(circumference))
console.log(radius.map(diameter))

// console.log(calculateCircle(radius, area))
// console.log(calculateCircle(radius, circumference))
// console.log(calculateCircle(radius, diameter))