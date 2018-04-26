// grab element by id, tag, and class

let theSearchBox = document.querySelector("#search-box");

let arrayOfParas = document.querySelectorAll("p");

let everythingUrgent = document.querySelectorAll(".urgent");

// See what an object can do
let theSearchBox = document.querySelector("#search-box");
console.dir(theSearchBox);


// Modifying Attributes
let logo = document.querySelector("#cat-photo");

let oldSrc = getAttribute("src");

logo.setAttribute("src", "http://placekitten.com/200")

// Changing Text
let mainHeading = document.querySelector("#main-heading");

mainHeading.innerHTML = "OMG so much javascript";

// Changing Element Styles
let theSearchBox = document.querySelector("#search-box");

theSearchBox.className = "urgent";

theSearchBox.style.color = "red";

// event Handler
let button = document.querySelector("#my-button");

function alertClick () {
    alert("stop clicking me!");
}

button.addEventListener('click', alertClick);

// event listeners are passed an event object

let button = document.querySelector("#my-button");

function alertClick(evt) {
    alert("stop clicking me!");
    console.dir(evt);
}

button.addEventListener("click", alertClick);

// Preventing Defualt Action
let searchForm = document.querySelector("#search-form");

function flakySearch(evt) {
    alert("I don't feel like searching");
    evt.preventDefault();
}

searchForm.addEventListener("submit", flakySearch);

// jQuery Selectors

// Javascript

document.querySelector("#search-box");
document.querySelectorAll("p");
document. querySelectorAll(".urgent");

// Javascript with JQuery
$("#search-box")
$("p")
$(".urgent")

// Changing CSS classes

$("#into-par").addClass("fancy");  // no error if already there
$("#into-par").hasClass("fancy"); // returns True or False
$("#into-par").removeClass("fancy"); // no error if not there
$("p").addClass("fancy"); // adds this class to all paragraphs

// Changing HTML Attributes
$("img#cat-photo").attr("src"); // returns src Attribute
$("img#cat-photo").attr("src", "cat.jpg") // add or change

// Changing contents of existing HTML elements
$("#bright").html(); // returns HTML
$("#bright").html("Hi"); // sets HTML to hi

// removing HTML elements
$("ul").empty(); // removes children -- UL tags will still be there
$("ul").remove(); // remove this element and its children-- this will remove all the UL tags aswell

// Showing/ hiding elements
$("img").hide(); // keeps the element but hides it
$("img").show(); // show element

// JQuery Event Listeners
function alertMe(evt) {
    alert("dont clickt that, please.");
}

// in Plain Javascript

let myButton = document.querySelector("#my-button");
myButton.addEventListener('click', alertMe);

// click event using JQUery
$("#my-button").on('click', alertMe);
