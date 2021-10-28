console.log("Start")

await setTimeout(function cb() {
    console.log("Inside of setTimeout")
}, 2000);

// fetch('https://jsonplaceholder.typicode.com/todos')
//     .then(function cbF() {
//         console.log("Callback Json placeholder")
//     })
//
//
// document.getElementById('clickMe').addEventListener('click', function cb() {
//     console.log("Button Clicked");
// })
// let startTime = new Date().getSeconds()
// let endTime = startTime
// while(endTime - startTime < 3) {
//     // console.log(endTime - startTime)
//     endTime = new Date().getSeconds()
// }
console.log("End")