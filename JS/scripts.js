alert("Javascript is working!");
console.log("Javascript is working!");

let button = document.getElementById("testButton");
button.addEventListener("click",function() {
    let buttonValue = button.value;
    console.log(buttonValue+" button was clicked!");
});