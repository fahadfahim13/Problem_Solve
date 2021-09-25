function reverse_words(str){
    return str.split(' ').reverse().join(' ')
}

let str = 'Hello World Again !!'
console.log(reverse_words(str))
