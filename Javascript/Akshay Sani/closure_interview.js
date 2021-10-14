function bigOuter(c){
    function outer(b) {
        function inner() {
            console.log(a, b, c)
        }
        let a = "Hello"
        return inner
    }
    return outer
}
var func = bigOuter(12)(5)
func()
