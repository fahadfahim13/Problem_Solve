function x() {
    for(var i = 1; i <= 5; i++){
        function close(num){
            setTimeout(() => {
                console.log(num)
            }, 1000)
        }
        close(i)
    }
}

x()