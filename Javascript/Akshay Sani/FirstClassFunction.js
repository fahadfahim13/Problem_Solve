console.log(a)
console.log(b)


// Function Statement
function a() {
    console.log("A called")
}
a()
// Function Expression
var b = function x() {
    console.log("B called");
    console.log(x)
};

b();

function c(param1, param2) {
    console.log(param1)
    console.log(param2)
}

var argument1 = 5;
var argument2 = 10;
c(argument1, argument2)