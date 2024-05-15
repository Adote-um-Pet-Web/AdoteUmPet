
document.addEventListener("DOMContentLoaded", function () {

    const slidersContainer = document.getElementById("sliders");
    const slides = document.querySelectorAll(".slide");
    const sliderStatus = document.getElementById("sliderStatus");


    let currentSlide = 0;
    let slideInterval = setInterval(nextSlide, 3000);


    function updateSliderStatus() {
        sliderStatus.innerHTML = "";
        slides.forEach((_, index) => {
            const dot = document.createElement("span");
            dot.classList.add("dot");
            if (index === currentSlide) {
                dot.classList.add("active");
            }
            dot.addEventListener("click", () => {
                goToSlide(index);
            });
            sliderStatus.appendChild(dot);
        });
    }


    function nextSlide() {
        currentSlide = (currentSlide + 1) % slides.length;
        goToSlide(currentSlide);
    }


    function goToSlide(index) {
        currentSlide = index;

        slides.forEach((slide) => {
            slide.classList.remove("active");
        });

        slides[currentSlide].classList.add("active");
        updateSliderStatus();
    }

    goToSlide(0);


    bannerArea.addEventListener("mouseenter", () => {
        clearInterval(slideInterval);
    });

    bannerArea.addEventListener("mouseleave", () => {
        slideInterval = setInterval(nextSlide, 3000);
    });

    updateSliderStatus();
});
