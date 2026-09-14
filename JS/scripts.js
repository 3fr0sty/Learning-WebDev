console.log("Javascript is working!");

// --- About page: toggle the hidden image when the test button is clicked ---
let button = document.getElementById("testButton");
if (button) {
    button.addEventListener("click", function () {
        let buttonValue = button.value;
        console.log(buttonValue + " button was clicked!");
        let image = document.getElementById("goodison");
        image.hidden = !image.hidden;
    });
}

// --- Contact page: show a thank-you message on submit (no backend call yet) ---
let form = document.getElementById("contactForm");
if (form) {
    let message = document.getElementById("formMessage");
    form.addEventListener("submit", function (event) {
        event.preventDefault();
        let name = document.getElementById("name").value;
        message.textContent = "Thank you " + name;
        message.hidden = false;
    });
}

// --- Signup page: check passwords match client-side, then POST to /signup.html ---
let signupForm = document.getElementById("signupForm");
if (signupForm) {
    signupForm.addEventListener("submit", function (event) {
        event.preventDefault();
        let password = document.getElementById("password").value;
        let confPassword = document.getElementById("confPassword").value;
        let message = document.getElementById("signupMessage");

        if (password !== confPassword) {
            message.textContent = "Passwords do not match.";
            message.hidden = false;
            return;
        }

        fetch("/signup.html", {
            method: "POST",
            body: new FormData(signupForm)
        })
            .then(function (response) {
                return response.json();
            })
            .then(function (data) {
                message.textContent = data.message;
                message.hidden = false;
            });
    });
}

// --- Login page: POST credentials to /login.html and show the server's response ---
let loginForm = document.getElementById("loginForm");
if (loginForm) {
    loginForm.addEventListener("submit", function (event) {
        event.preventDefault();
        let message = document.getElementById("loginMessage");

        fetch("/login.html", {
            method: "POST",
            body: new FormData(loginForm)
        })
            .then(function (response) {
                return response.json();
            })
            .then(function (data) {
                message.textContent = data.message;
                message.hidden = false;

                if (data.success) {
                    window.location.href = "index.html";
                }
            });
    });
}

let signOutButton = document.getElementById("signOut")
if (signOutButton) {
    signOutButton.addEventListener("click", function (event) {
        event.preventDefault()
        fetch("/signout")
        .then(function(response) {
            return response.json();
        })
        .then(function(data) {
            if (data.sign_out_success) {
                window.location.href = "index.html";
            }
       });
    });
}

let loginLink = document.getElementById("loginLink")
let welcomeMessage = document.getElementById("welcomeMessage")
if (welcomeMessage) {
    fetch("/whoami")
    .then(function(response) {
        return response.json()
    })
    .then(function(data) {
        if (data.logged_in_as) {
            let user = data.logged_in_as
            welcomeMessage.textContent = "Welcome, " + user;
            loginLink.textContent = "Logged in as " + user;
            welcomeMessage.hidden = false
            signOutButton.hidden = false
        }
    });
}

