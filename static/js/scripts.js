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

    const isAuthenticated = document.querySelector('.characters-container').dataset.authenticated === 'true';
    const likeButtons = document.querySelectorAll('.like-button');

    likeButtons.forEach(button => {
        button.addEventListener('click', function () {
            // Check if the user is authenticated before allowing the like action
            if (!isAuthenticated) {
                alert("You must be logged in to like a character.");
                return; // Prevent the action if not authenticated
            }

            // Toggle button text and icon between Like and Liked
            if (this.textContent.trim() === "Like") {
                this.innerHTML = '<i class="fa-solid fa-thumbs-up"></i> Liked'; // Change to Liked
            } else {
                this.innerHTML = '<i class="fa-regular fa-thumbs-up"></i> Like'; // Change back to Like
            }
        });
    });

    // Comment section toggle functionality
    const commentButton = document.querySelectorAll('.comment-button');

    commentButton.forEach(button => {
        button.addEventListener('click', function () {
            // Find the closest character box and select the next sibling (comment section)
            const commentSection = this.closest('.character-box').nextElementSibling;

            // Toggle visibility by adding/removing the 'hidden' class
            commentSection.classList.toggle('hidden');
        });
    });
});