console.log("Start")

setTimeout(function cb() {
    console.log("Inside of setTimeout")
}, 2000);

fetch('https://jsonplaceholder.typicode.com/todos')
    .then(function cbF() {
        console.log("Callback Json placeholder")
    })


// document.getElementById('clickMe').addEventListener('click', function cb() {
//     console.log("Button Clicked");
// })

console.log("End")