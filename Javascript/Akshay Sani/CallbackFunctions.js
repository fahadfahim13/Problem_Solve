setTimeout(function() {
    console.log("Timer")
}, 3000)

function outerFunction(cb){
    console.log("Calling Callback Function")
    cb()
}

outerFunction(function y(){
    console.log("I am a callback function")
})