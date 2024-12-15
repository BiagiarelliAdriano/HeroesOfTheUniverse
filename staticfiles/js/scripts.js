const classtoggleButton = document.getElementById("toggle-class-image-btn");
const classImageDiv = document.querySelector(".class-image-section");

// Toggle Visibility For Class Image Div
if (classtoggleButton) {
    classtoggleButton.addEventListener("click", function () {
        classImageDiv.classList.toggle("hidden");
    });
}

// Toggle Visibility For Spell List Div
const spelltoggleButton = document.getElementById("toggle-spell-list-btn");
const spellListDiv = document.querySelector(".spell-list-section");

if (spelltoggleButton) {
    spelltoggleButton.addEventListener("click", function () {
        spellListDiv.classList.toggle("hidden");
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

    // Character Sheet Pagination functionality
    const paginationButtons = document.querySelectorAll(".pagination-btn");
    const pages = document.querySelectorAll(".page-content");

    paginationButtons.forEach(button => {
        button.addEventListener("click", () => {
            pages.forEach(page => page.classList.remove("active"));

            const pageId = `page-${button.getAttribute("data-page")}`;
            document.getElementById(pageId).classList.add("active");
        });
    });

    // Show deletion modal functionality
    const deleteButtons = document.querySelectorAll('.delete-character-btn');
    const modal = document.querySelector('.delete-modal');
    const deleteForm = document.querySelector('.delete-character-form');
    const cancelButton = document.querySelector('.close-modal');

    deleteButtons.forEach(button => {
        button.addEventListener('click', function () {
            const characterId = this.getAttribute('data-character-id');
            deleteForm.action = `/universe/character/delete/${characterId}/`; // Update form action
            modal.classList.remove('hidden'); // Show the modal
        });
    });

    cancelButton.addEventListener('click', function () {
        modal.classList.add('hidden'); // Hide the modal
    });

});