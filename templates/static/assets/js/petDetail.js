let mainPhoto = document.getElementById("mainPhoto");
let modal = document.getElementById("modal");
let modalImage = document.getElementById("modalImage");
let galleryImages = document.querySelectorAll(".gallery-thumbnails img");
let currentIndex = 0;
let timer;

function changePhoto(imgElement) {
    mainPhoto.src = imgElement.src;
    currentIndex = Array.from(galleryImages).indexOf(imgElement);
    resetTimer();
}

mainPhoto.onclick = function () {
    modal.style.display = "flex";
    modalImage.src = this.src;
};

function closeModal() {
    modal.style.display = "none";
}

function nextPhoto() {
    currentIndex = (currentIndex + 1) % galleryImages.length;
    mainPhoto.src = galleryImages[currentIndex].src;
}

function prevPhoto() {
    currentIndex =
        (currentIndex - 1 + galleryImages.length) % galleryImages.length;
    mainPhoto.src = galleryImages[currentIndex].src;
}

function modalNextPhoto() {
    currentIndex = (currentIndex + 1) % galleryImages.length;
    modalImage.src = galleryImages[currentIndex].src;
}

function modalPrevPhoto() {
    currentIndex =
        (currentIndex - 1 + galleryImages.length) % galleryImages.length;
    modalImage.src = galleryImages[currentIndex].src;
}

function resetTimer() {
    clearInterval(timer);
    timer = setInterval(nextPhoto, 10000);
}

function setupTabs() {
    const tabButtons = document.querySelectorAll(".tab-btn");
    const tabContents = document.querySelectorAll(".tab-content");

    tabButtons.forEach((button) => {
        button.addEventListener("click", () => {
            tabButtons.forEach((btn) => btn.classList.remove("active"));
            tabContents.forEach((content) =>
                content.classList.remove("active")
            );

            button.classList.add("active");

            const tabId = button.getAttribute("data-tab") + "-tab";
            document.getElementById(tabId).classList.add("active");
        });
    });
}

document.addEventListener("DOMContentLoaded", (event) => {
    timer = setInterval(nextPhoto, 10000);
    setupTabs();

    modal.addEventListener("click", (e) => {
        if (e.target === modal) {
            closeModal();
        }
    });

    document.addEventListener("keydown", (e) => {
        if (modal.style.display === "flex") {
            if (e.key === "Escape") {
                closeModal();
            } else if (e.key === "ArrowRight") {
                modalNextPhoto();
            } else if (e.key === "ArrowLeft") {
                modalPrevPhoto();
            }
        }
    });
});
