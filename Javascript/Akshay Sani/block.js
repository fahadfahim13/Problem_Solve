var a = 100
let b = 200
const c = 300
{
    var a = 10
    let b = 20
    const c = 30
    console.log(a)
    console.log(b)
    console.log(c)
    {
        var a = 400
        const c = 300
        console.log(a)
        console.log(c)
    }
}

console.log(a)
console.log(b)
console.log(c)