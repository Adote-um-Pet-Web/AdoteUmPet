// abertura e fechamento do filtro
document.addEventListener("DOMContentLoaded", function () {
    document.querySelector("#filtro").addEventListener("click", function () {
        var navbar = document.querySelector(".navbar");
        var arrow = document.querySelector("#arrow");

        var computedStyle = window.getComputedStyle(navbar);
        var display = computedStyle.getPropertyValue("display");

        if (display === "none") {
            navbar.style.display = "flex";
            navbar.style.animation = "slideLeft 0.3s ease forwards";
            arrow.innerHTML = "&#x25B4;";
        } else if (display === "flex") {
            navbar.style.animation = "slideRight 0.3s ease forwards";
            setTimeout(() => {
                navbar.style.display = "none";
                arrow.innerHTML = "&#x25BE;";
            }, 300);
        }
    });
    document.querySelector("#filtroM").addEventListener("click", function () {
        var navbarM = document.querySelector(".navbar");
        var arrowM = document.querySelector("#arrowM");

        var computedStyle = window.getComputedStyle(navbarM);
        var display = computedStyle.getPropertyValue("display");

        if (display === "none") {
            navbarM.style.display = "flex";
            arrowM.innerHTML = "&#x25B4;";
        } else if (display === "flex") {
            navbarM.style.display = "none";
            arrowM.innerHTML = "&#x25BE;";
        }
    });
});
function showBreeds(species) {
    var breedListDog = document.getElementById("breedListDog");
    var breedListCat = document.getElementById("breedListCat");
    var dogCheckbox = document.getElementById("dog");
    var catCheckbox = document.getElementById("cat");

    if (species === "dog") {
        breedListDog.style.display = dogCheckbox.checked ? "flex" : "none";
    } else if (species === "cat") {
        breedListCat.style.display = catCheckbox.checked ? "flex" : "none";
    }
}

function toggleListVisibility(listId, spanId) {
    var list = document.getElementById(listId);
    var span = document.getElementById(spanId);
    list.classList.toggle("hidden");
    if (!list.classList.contains("hidden")) {
        span.innerHTML = "&#x25B4;";
    } else {
        span.innerHTML = "&#x25BE;";
    }
}

document.getElementById("speciesTitle").addEventListener("click", function () {
    toggleListVisibility("speciesList", "speciesTitleArrow");
});

document.getElementById("sizeTitle").addEventListener("click", function () {
    toggleListVisibility("sizeList", "sizeTitleArrow");
});

document.getElementById("ageTitle").addEventListener("click", function () {
    toggleListVisibility("ageList", "ageTitleArrow");
});


document.getElementById("genderTitle").addEventListener("click", function () {
    toggleListVisibility("genderList", "genderTitleArrow");
});
