
//banner
document.addEventListener("DOMContentLoaded", function () {
    const bannerArea = document.getElementById("bannerArea");
    const slidersContainer = document.getElementById("sliders");
    const slides = document.querySelectorAll(".slide");
    const sliderStatus = document.getElementById("sliderStatus");

    let currentSlide = 0;
    let slideInterval;
    const slideDuration = 5000; 
    let isHovering = false;
    let touchStartX = 0;
    let touchEndX = 0;

    function initSlider() {
        goToSlide(0);
        startSlideInterval();
        updateSliderStatus();
        addEventListeners();
    }

    function addEventListeners() {
        bannerArea.addEventListener("mouseenter", pauseSlider);
        bannerArea.addEventListener("mouseleave", resumeSlider);

        slidersContainer.addEventListener(
            "touchstart",
            handleTouchStart,
            false
        );
        slidersContainer.addEventListener("touchend", handleTouchEnd, false);
    }

    function handleTouchStart(e) {
        touchStartX = e.changedTouches[0].screenX;
        pauseSlider();
    }

    function handleTouchEnd(e) {
        touchEndX = e.changedTouches[0].screenX;
        handleSwipe();
        resumeSlider();
    }

    function handleSwipe() {
        if (touchEndX < touchStartX - 50) {
            nextSlide();
        } else if (touchEndX > touchStartX + 50) {
            prevSlide();
        }
    }

    function prevSlide() {
        currentSlide = (currentSlide - 1 + slides.length) % slides.length;
        goToSlide(currentSlide);
    }

    function nextSlide() {
        currentSlide = (currentSlide + 1) % slides.length;
        goToSlide(currentSlide);
    }

    function goToSlide(index) {
        currentSlide = index;

        slides.forEach((slide) => {
            slide.style.opacity = 0;
            slide.classList.remove("active");
        });

        slides[currentSlide].classList.add("active");
        setTimeout(() => {
            slides[currentSlide].style.opacity = 1;
        }, 10);

        updateSliderStatus();
    }

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

    function startSlideInterval() {
        clearInterval(slideInterval);
        slideInterval = setInterval(nextSlide, slideDuration);
    }

    function pauseSlider() {
        clearInterval(slideInterval);
        isHovering = true;
    }

    function resumeSlider() {
        if (!isHovering) return;
        clearInterval(slideInterval);
        slideInterval = setInterval(nextSlide, slideDuration);
        isHovering = false;
    }

    function addNavigationButtons() {
        const prevBtn = document.createElement("button");
        prevBtn.innerHTML = "❮";
        prevBtn.classList.add("slider-nav", "prev");
        prevBtn.addEventListener("click", prevSlide);

        const nextBtn = document.createElement("button");
        nextBtn.innerHTML = "❯";
        nextBtn.classList.add("slider-nav", "next");
        nextBtn.addEventListener("click", nextSlide);

        slidersContainer.appendChild(prevBtn);
        slidersContainer.appendChild(nextBtn);
    }

    initSlider();
    addNavigationButtons();
});
