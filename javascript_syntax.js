////////////////////////////// Pick a secret number ////////////////////////////

// Math.floor() returns the largest integer less than or equal to
// a given number
// Math.floor(5.95) --> 5
// Math.floor(5.04) --> 5
// Math.floor(-5.05) --> -6

// Math.random() generates a random decimal
// multiply that random decimal by 100

let myNumber = Math.floor(Math.random() * 100);

function guessMyNumber(guess) {

    if (guess < myNumber) {
        console.log("Too low!");
    } else if (guess > myNumber) {
        console.log("Too high!");
    } else {
        console.log("yay!!");
    }
}

// take a wild guess
guessMyNumber(60);

///////////////////////////////// Variables /////////////////////////////////////


let totalScore;
let userScore = 20;
let bonusPoints = 30;
let userCity = "Toronto";

// let can be reassinged
total score = userScore + bonusPoints;
userCity = "San Francisco"; 

const nums = [3, 4, 5, 6];
// push method adds a new item to an array, and returns the new length
// the new item will be added to the end of the array
// array.push(item 1, item 2...) you can add many things to the array
nums.push(9); // okay!

nums = [7, 8, 9] // error.. you cant reassing a const variable in JS

//////////////////////////////////// Summary //////////////////////////////////////

// have to declare once
let userScore, userCity;
userScore = 5;
userCity = "SF";
// or you can declare and assign at once
let userScore = 10;
let userCity = "Toronto";

const userBirthday = "January 15";

const birthdays = ["January 15"];
// its okay to mutate the values, but you cant reassign a constant variable
birthdays.push("March 21");


/////////////////////////// Control Flows: Conditionals /////////////////////////

if (x > 7) {
    console.log("too big");
} else if (x < 1) {
    console.log("too small");
} else {
    console.log("just right");
}

// Braces are not needed for single line-clauses

// you could write it like this
if (x > 7) {
    console.log("too big");
} else if (x < 1) {
    console.log("too small");
}

// but you could also leave out the Braces
if (x > 7)
    console.log("too big");
else if (x < 1)
    console.log("too small");

// without the braces, javascript only consideres the first line
// with the cnosole.log to be attatched to the if

if (name === "Balloonicorn")
    console.log("hi");
    score += 10;



/////////////////////////// While Loops /////////////////////////

let i = 0;
while (i < 5) {
    console.log(i);
    i += 1;
}


/////////////////////////// Function Declarations /////////////////////////

function multiply(x, y) {
    return x * y;
}

multiply(3, 7);

// defualt values

function add(x, y=0) {
    return x + y;
}


/////////////////////////// Strings/ String Formatting /////////////////////////

let name = "Jane";
let role = 'engineer';

let message = `Hello ${name}!`;


///////////////////////////////////// Arrays //////////////////////////////////////

const states = ["MD", "VA", "CA"];

states.push("NY");

states[2]; // 'CA'
states.slice(2); // ['CA', 'NY']
states.slice(2, 3); // ['CA']

states.includes("NY"); // True
states.includes("NH"); // False



////////////////////////////////// Looping over Arrays //////////////////////////////////////

let states = ["MD", "VA", "CA"];

// looping over items

for (let state of states) {
    console.log(`I love ${state}!`);
}

// looping over using indices

for (let i = 0; i < states.length; i += 1) {
    console.log(`I love ${states[i]}`);
}



////////////////////////////////// Maps  /////////////////////////////////////////

let capitals = new Map([
    ['MD', 'Annapolis'], 
    ['CA', 'Sacramento'], 
    ['OR', 'Salem']
    ]);

capitals.set('Ny', 'Albany');
capitals.get('CA'); // 'Sacramento'
capitals.has('OR'); // True

// Alternatively, we can create an empty map
let stateCapitals = new Map();

// returns an iterator object so we cant index into it
// but we can loop over it
vapitals.entries();
capitals.keys(); 
capitals.values();
capitals.size(); // 4

if capitals.has("CA") {
    console.log("California");
}

for (let k of capitals) {
    console.log(`${k[0]} is the capital of ${k[1]}`);
    console.log(k[0] + " is the capital of " + k[1]);
}



////////////////////////////////// Objects  /////////////////////////////////////

const cat = {
    "name": "Anna", 
    "color": "tabby",
    "Age": 5
};

cat.disposition = 'mad';
cat['name']; // "Anna"
cat.name // Anna

Object.keys(cat);
Object.values(cat);
Object.entries(cat);

// These methods returns an array of a given object's keys, values, and entries
// respectively

for (let k in cat) {
    console.log(cat[k]);

}

var capitals = {
    MD: "Annapolis";
}

////////////////////////////////// semi-Colons  /////////////////////////////////////

if (x === 1) {
    console.log(x);
}; else {           // this will throw an error it will get read as an empty expression
    console.log("not one");
}
