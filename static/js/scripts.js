// Function to show hidden buttons when the title button is clicked
function showButtons() {
    const hiddenButtons = document.getElementById('hidden-buttons');
    hiddenButtons.style.display = 'flex'; // Show hidden buttons
}

// Function to toggle visibility
document.addEventListener("DOMContentLoaded", function () {
    const buttonsContainer = document.getElementById("buttons-container");
    const registerForm = document.getElementById("register-form");
    const showRegisterFormButton = document.getElementById("show-register-form")

    showRegisterFormButton.addEventListener("click", function () {
        buttonsContainer.style.display = "none";
        registerForm.style.display = "block";
    });
});