document.getElementById("login-btn").addEventListener("click", function() {
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;
    const errorMessage = document.getElementById("error-message");


    const validUsers = [
        { username: "standard_user", password: "secret_sauce" },
        { username: "locked_out_user", password: "sauce_secret" },
        { username: "problem_user", password: "user_123" },
        { username: "performance_glitch_user", password: "secret_sauce" },
        { username: "demo_user", password: "demo_pass" }
    ];

    const isValid = validUsers.some(user => user.username === username && user.password === password);

    if (isValid) {
        //alert("Login Successful!");
        window.location.href = "dashboard.html";  
    } else {
        errorMessage.textContent = "Invalid Username or Password!";
        errorMessage.style.display = "block";
    }
});
