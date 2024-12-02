// Function to show hidden buttons when the title button is clicked
function showButtons() {
    const hiddenButtons = document.getElementById('hidden-buttons');
    hiddenButtons.style.display = 'flex'; // Show hidden buttons
}

// Function to toggle visibility
document.addEventListener("DOMContentLoaded", function () {
    const buttonsContainer = document.getElementById("buttons-container");
    const registerForm = document.getElementById("register-form");
    const loginForm = document.getElementById("login-form");

    const showRegisterFormButton = document.getElementById("show-register-form");
    const showLoginFormButton = document.getElementById("show-login-form");

    // Show register form and hide buttons
    showRegisterFormButton.addEventListener("click", function () {
        buttonsContainer.style.display = "none";
        registerForm.style.display = "block";
    });

    // Show login form and hide buttons
    showLoginFormButton.addEventListener("click", function () {
        buttonsContainer.style.display = "none";
        loginForm.style.display = "block";
    });
});