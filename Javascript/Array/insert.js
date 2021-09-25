const insertFirst = (arr, item) => {
    arr.splice(0, 0, item)
    return arr
}

const insertLast = (arr, item) => {
    arr.push(item)
    return arr
}

const insertAt = (arr, idx, item) => {
    arr.splice(idx - 1, 0, item)
    return arr
}

let arr = [1, 2, 3, 5]
console.log(insertFirst(arr, 0))
console.log(insertFirst(arr, 4))
console.log(insertLast(arr, 6))
console.log(insertAt(arr, 4, 13))
