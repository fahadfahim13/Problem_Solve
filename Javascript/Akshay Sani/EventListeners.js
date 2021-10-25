function attachEventListener(){
    let count = 0;

    document.getElementById("clickMe")
        .addEventListener("click",
            function clickMe() {
            console.log("Button Clicked", ++count)
        })
}

attachEventListener()