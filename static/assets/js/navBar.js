
function showBreeds(species) {
    var breedListDog = document.getElementById("breedListDog");
    var breedListCat = document.getElementById("breedListCat");
    var dogCheckbox = document.getElementById("dog");
    var catCheckbox = document.getElementById("cat");

    if (species === "dog") {
        breedListDog.style.display = dogCheckbox.checked ? "block" : "none";
    } else if (species === "cat") {
        breedListCat.style.display = catCheckbox.checked ? "block" : "none";
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

document
    .getElementById("deficiencyTitle")
    .addEventListener("click", function () {
        toggleListVisibility("deficiencyList", "deficiencyTitleArrow");
    });

document.getElementById("genderTitle").addEventListener("click", function () {
    toggleListVisibility("genderList", "genderTitleArrow");
});
