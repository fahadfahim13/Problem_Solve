const deleteFirst = (arr) => {
    arr.splice(0, 1)
    return arr
}

const deleteLast = (arr) => {
    arr.splice(arr.length - 1, 1)
    return arr
}

const deleteAt = (arr, pos) => {
    arr.splice(pos - 1, 1)
    return arr
}

const search = (arr, num) => {
    return arr.findIndex((el) => el === num)
}

let arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
console.log(deleteFirst(arr))
console.log(deleteFirst(arr))
console.log(deleteLast(arr))
console.log(deleteLast(arr))

console.log(deleteAt(arr, 5))
console.log(search(arr, 40))