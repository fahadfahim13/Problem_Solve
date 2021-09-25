function rev(str){
    return str.split('').reverse().join('')
}

function reverse(string){
    let str = string.split('')
    for(let i = 0, j = str.length; i<str.length/2, j>(str.length/2) - 1; i++, j--){
        let tmp = str[i]
        str[i] = str[j]
        str[j] = tmp
    }
    return str.join('')
}


let str = "Hello World"
console.log(rev(str))
console.log(reverse(str))