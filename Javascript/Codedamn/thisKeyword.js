console.log("Howdy");

saySomething("Hello","Hi");
// Uncaught SyntaxError: Duplicate parameter name not
// allowed in this context

var gp = document.querySelector(".gp")
var p = document.querySelector(".parent")
var c = document.querySelector('.child')

gp.addEventListener('click', () => {
    console.log("Grand Parent Clicked")
})

p.addEventListener('click', () => {
    console.log("Parent Clicked")
})

c.addEventListener('click', () => {
    console.log("Child Clicked")
})

function parentClick(){
    console.log("Parent Clicked")
}

function childClick(){
    console.log("Child Clicked")
}

function saySomething(greeting,greeting) {
    // "use strict";
    console.log(greeting);
}


const obj = {
    myFunc() {
        console.log(this)
    },
    myFunc3() {
        function myFunc4(){
            console.log(this)
        }
        return myFunc4()
    }
}
//
// function myFunc2() {
//     console.log(this)
// }
//
// const test1 = obj.myFunc
// test1()
// test1() -> Gives us global
// obj.myFunc() -> Gives us obj
// obj.myFunc3() -> Gives us global
// obj.myFunc3()