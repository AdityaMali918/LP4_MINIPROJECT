// document.getElementById("register-btn").addEventListener("click", function(event) {
//     event.preventDefault();

//     // Retrieve input values
//     let username = document.getElementById("username").value;
//     let email = document.getElementById("email").value;
//     let password = document.getElementById("password").value;
//     let confirmPassword = document.getElementById("confirm-password").value;

//     // Define regular expressions for validation
//     let usernameRegex = /^[a-z0-9]{3,20}$/;
//     let emailRegex = /^[^@\s]+@[^@\s]+\.[^@\s]+$/;
//     let passwordRegex = /^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$/;

//     let isValid = true;

//     // Validate username
//     if (!usernameRegex.test(username)) {
//         document.getElementById("username-error").textContent = "Username must be 3-20 alphanumeric characters.";
//         isValid = false;
//     } else {
//         document.getElementById("username-error").textContent = "";
//     }

//     // Validate email
//     if (!emailRegex.test(email)) {
//         document.getElementById("email-error").textContent = "Invalid email format.";
//         isValid = false;
//     } else {
//         document.getElementById("email-error").textContent = "";
//     }

//     // Validate password
//     if (!passwordRegex.test(password)) {
//         document.getElementById("password-error").textContent = "Password must be at least 8 characters long, contain at least one letter and one number.";
//         isValid = false;
//     } else {
//         document.getElementById("password-error").textContent = "";
//     }

//     // Validate confirm password
//     if (password !== confirmPassword) {
//         document.getElementById("confirm-password-error").textContent = "Passwords do not match.";
//         isValid = false;
//     } else {
//         document.getElementById("confirm-password-error").textContent = "";
//     }

//     // Display success message or hide it based on validation
//     if (isValid) {
//         document.getElementById("success-message").style.display = "block";
//         document.getElementById("error-message").textContent = ""; // Clear any previous error message
//     } else {
//         document.getElementById("success-message").style.display = "none";
//         document.getElementById("error-message").textContent = "Please correct the errors above."; // Show a generic error message
//     }
// });


document.getElementById("register-btn").addEventListener("click", function(event) {
    event.preventDefault();

    // Retrieve input values
    let username = document.getElementById("username").value;
    let email = document.getElementById("email").value;
    let password = document.getElementById("password").value;
    let confirmPassword = document.getElementById("confirm-password").value;

    // Define regular expressions for validation
    let usernameRegex = /^[a-zA-Z0-9]{3,20}$/; // Updated regex
    let emailRegex = /^[^@\s]+@[^@\s]+\.[^@\s]+$/;
    let passwordRegex = /^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$/;

    let isValid = true;

    // Validate username
    if (!usernameRegex.test(username)) {
        document.getElementById("username-error").textContent = "Username must be 3-20 alphanumeric characters.";
        isValid = false;
    } else {
        document.getElementById("username-error").textContent = "";
    }

    // Validate email
    if (!emailRegex.test(email)) {
        document.getElementById("email-error").textContent = "Invalid email format.";
        isValid = false;
    } else {
        document.getElementById("email-error").textContent = "";
    }

    // Validate password
    if (!passwordRegex.test(password)) {
        document.getElementById("password-error").textContent = "Password must be at least 8 characters long, contain at least one letter and one number.";
        isValid = false;
    } else {
        document.getElementById("password-error").textContent = "";
    }

    // Validate confirm password
    if (password !== confirmPassword) {
        document.getElementById("confirm-password-error").textContent = "Passwords do not match.";
        isValid = false;
    } else {
        document.getElementById("confirm-password-error").textContent = "";
    }

    // Display success message or hide it based on validation
    if (isValid) {
        document.getElementById("success-message").style.display = "block";
        document.getElementById("error-message").textContent = ""; // Clear any previous error message
    } else {
        document.getElementById("success-message").style.display = "none";
        document.getElementById("error-message").textContent = "Please correct the errors above."; // Show a generic error message
    }
});
