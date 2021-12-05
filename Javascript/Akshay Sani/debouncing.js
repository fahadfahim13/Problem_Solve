let counter = 0;

const getdata = () => {
    console.log("Get Something", counter++);
}

const debounce = (fn, delay) => {
    let timer;
    return function() {
        let context = this, args = arguments;
        clearTimeout(timer)
        timer = setTimeout(() => {
            fn.apply(context, args);
        }, delay);

    }
}

const getBetterData = debounce(getdata, 500);

const click = (e) => {
    console.log("Clicked purchase: ", e.target);
}

const debounceMethod = (fn, delay) => {
    let timeoutId;
    return function (...args) {
        if(timeoutId) clearTimeout(timeoutId);
        timeoutId = setTimeout(() => {
            fn(...args);
        }, delay)
    }
}

const throttle = (fn, delay) => {
    let last = 0;
    return function (...args) {
        const now = new Date().getTime();
        if (now - last < delay){
            return
        }
        last = now;
        fn(...args);
    }
}

document.getElementById('myId').addEventListener("click", debounceMethod(e => click(e), 2000))

document.getElementById('throttle').addEventListener("click", throttle(e => click(e), 2000))
