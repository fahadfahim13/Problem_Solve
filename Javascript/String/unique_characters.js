function number_unique_char(str){
    let s = new Set()
    str.split('').map((chr) => {
        if(chr !== ' ') s.add(chr.toUpperCase())
    })
    return s
}

function unique_chars(str){
    let ans = {}
    let num = 0
    str.split('').map((chr) => {
        if(chr!==' ' && !ans[chr]) {
            ans[chr] = 1
            num++;
        }
    })
    return num
}

let str = "Hello World"
let ans = number_unique_char(str)
console.log(ans, ans.size)
console.log(unique_chars(str))