let mainPhoto = document.getElementById('mainPhoto');
let modal = document.getElementById('modal');
let modalImage = document.getElementById('modalImage');
let galleryImages = document.querySelectorAll('.gallery img');
let currentIndex = 0;
let timer;

function changePhoto(imgElement) {
    mainPhoto.src = imgElement.src;
    currentIndex = Array.from(galleryImages).indexOf(imgElement);
    resetTimer();
}

mainPhoto.onclick = function() {
    modal.style.display = "flex";
    modalImage.src = this.src;
}

function closeModal() {
    modal.style.display = "none";
}

function nextPhoto() {
    currentIndex = (currentIndex + 1) % galleryImages.length;
    mainPhoto.src = galleryImages[currentIndex].src;
}

function resetTimer() {
    clearInterval(timer);
    timer = setInterval(nextPhoto, 10000);
}

document.addEventListener('DOMContentLoaded', (event) => {
    timer = setInterval(nextPhoto, 10000);
});
