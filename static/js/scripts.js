const classtoggleButton = document.getElementById("toggle-class-image-btn");
const classImageDiv = document.querySelector(".class-image-section");

// Toggle Visibility For Class Image Div
if (classtoggleButton) {
    classtoggleButton.addEventListener("click", function () {
        classImageDiv.classList.toggle("hidden");
    });
}

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

    const imagePreview = document.getElementById('class-image-preview');
    const radioButtons = document.querySelectorAll('#class-image-selector input[type="radio"]');

    // Show register form and hide buttons
    if (showRegisterFormButton) {
        showRegisterFormButton.addEventListener("click", function () {
            buttonsContainer.style.display = "none";
            registerForm.style.display = "block";
        });
    }

    // Show login form and hide buttons
    if (showLoginFormButton) {
        showLoginFormButton.addEventListener("click", function () {
            buttonsContainer.style.display = "none";
            loginForm.style.display = "block";
        })
    }

    // Dynamically Change Class Image
    if (radioButtons.length > 0) {
        radioButtons.forEach(function (radioButtons) {
            radioButtons.addEventListener('change', function () {
                imagePreview.src = `/static/images/${this.value}.png`;
                imagePreview.alt = this.value;
            });
        });
    }
});