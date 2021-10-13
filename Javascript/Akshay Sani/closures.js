function x() {
    var a  = 7
    function z() {
        console.log("Hello")
    }
    function y() {
        z()
        console.log(a)
    }
    y()
    z()
}

x()
