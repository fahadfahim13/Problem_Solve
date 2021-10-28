function x() {
    for(let i = 1; i <= 5; i++){
        function close(num){
            setTimeout(() => {
                console.log(num)
            }, 1000)
        }
        close(i)
    }
}

x()
// for(let i = 1; i <= 5; i++){
//     setTimeout(() => {
//         console.log(i)
//     }, 0)
// }