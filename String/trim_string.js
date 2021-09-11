function trim_string(str){
    let a = 0, b = str.length - 1;
    for(let i = 0; i < str.length; i++){
        if(str[i] !== ' '){
            a = i;
            break;
        }
    }

    for(let j = str.length - 1; j >= 0; j--){
        if(str[j] !== ' '){
            b = j;
            break;
        }
    }

    let ans = ''
    for(let  i = a; i <= b; i++){
        ans =  ans + str[i];
    }
    return ans
}

let str = "               Hello    World!!        "
console.log(trim_string(str))
console.log(str.trim())