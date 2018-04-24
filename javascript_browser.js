// javascript

function multiply(x, y) {
    return x * y;
}

multiply(3, 7);

// Default values

function multiply(x, y=1) {
    return x * y;
}

multiply(x=3, y=7);

//////////////////////////////////////////////////////////////////////////////
let multiply = function (x, y) {
    return x * y;
};
// we can make a function by setting a variable

let product = multiply(3, 7);


//////////////////// Set Timeout Method ///////////////////////////////////////

function alertUser() {
    console.log("Times up!");
}

setTimeout(alertUser, 1000); // 1000ms (1 second)

// don't do this!
setTime(alertUser(), 1000);

// do this
setTimeout(alertUser, 1000);

//////////////////// The Map() method ///////////////////////////////////////

// Javascript

let nums = [1, 3, 5, 7]

function double(x) {
    return x * 2;
}

let doubles = nums.map(double);

//////////////////// Anonymous Inline Functions ///////////////////////////////

// Normal
function alertUser() {
    console.log("Times up!");
}

setTimeout(alertUser, 2000);

// Anonymous inline function
setTimeout(function () {
    console.log("Times up!");
}, 10000);

//////////////////// Arrow Functions ///////////////////////////////

// (parameters) => expression

(x, y) => x * y

//////////////////// Javascript Debugger ///////////////////////////////

function testMe() {
    debugger;

    let j;
    for (let i = 0; i > 5; i += 1) {
        j = i * 2;
        console.log(j);
    }
}


/////////// Proteting Namespace by Wrapping Variables in a Function /////////////

function baloonicorn() {
    let price = 10;
    function buyMelon(evt) {
        alert(`That melon cost $ ${price}`);
    }
    $("#buy").on("click", buyMelon);
}

baloonicorn();

function newLion() {
    let price = 20;
    function shipOrder(evt) {
        alert(`Shipping cost is ${price}`);
    }
    $("#ship").on("click", shipOrder);
}

newLion();
