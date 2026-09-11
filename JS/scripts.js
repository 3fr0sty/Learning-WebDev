console.log("Javascript is working!");

let button = document.getElementById("testButton");
if (button) {
    button.addEventListener("click",function() {
        let buttonValue = button.value;
        console.log(buttonValue+" button was clicked!");
        let image = document.getElementById("goodison");
        image.hidden = !image.hidden;
    });
}

let form = document.getElementById("contactForm");
if (form) {
    let message = document.getElementById("formMessage");
    form.addEventListener("submit", function(event){
        event.preventDefault();
        let name = document.getElementById("name").value;
        message.textContent = "Thank you " + name;
        message.hidden = false;
    });
}