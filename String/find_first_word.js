const find_first_word = (str) => {
    let words = str.split(' ')
    let ans = []
    for(let i = 0; i < words.length; i++){
        if(words[i]!==''){
            ans.push(words[i][0])
        }
    }
    return ans
}

console.log(find_first_word("         Hello World!! how are you?"))
