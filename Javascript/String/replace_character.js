function replace_character(str, pos, chr){
    let arr = str.split('')
    arr[pos] = chr
    return arr.join('');
}

let str =  "Hello World";
let pos = 4;
let chr = "a"

console.log(replace_character(str, pos, chr))
