// Help Modal Logic
document.addEventListener("DOMContentLoaded", () => {
    const helpButton = document.querySelector(".help-button button");
    const modal = document.getElementById("helpModal");
    const closeModal = document.querySelector(".close");

    // Open Modal
    helpButton.addEventListener("click", () => {
        modal.style.display = "block";
    });

    // Close Modal
    closeModal.addEventListener("click", () => {
        modal.style.display = "none";
    });

    // Close Modal When Clicking Outside
    window.addEventListener("click", (event) => {
        if (event.target === modal) {
            modal.style.display = "none";
        }
    });
});

