document.addEventListener("DOMContentLoaded", function () {
    const filterBtn = document.getElementById("filterBtn");
    const cards = document.querySelectorAll("#cards .card");
    const filterHeaders = document.querySelectorAll(".filter-header");

    filterHeaders.forEach((header) => {
        header.addEventListener("click", function () {
            const list = this.parentElement.querySelector("ul");
            const arrow = this.querySelector(".arrow");

            list.classList.toggle("hidden");
            arrow.style.transform = list.classList.contains("hidden")
                ? "rotate(0deg)"
                : "rotate(180deg)";
        });
    });

    filterBtn.addEventListener("click", function () {
        const selectedSpecies = [
            ...document.querySelectorAll(
                '#speciesList input[type="checkbox"]:checked'
            ),
        ].map((cb) => cb.value);
        const selectedBreeds = [
            ...document.querySelectorAll(
                '.breed-list input[type="checkbox"]:checked'
            ),
        ].map((cb) => cb.value.toLowerCase());
        const selectedSizes = [
            ...document.querySelectorAll(
                '#sizeList input[type="checkbox"]:checked'
            ),
        ].map((cb) => cb.value);
        const selectedAges = [
            ...document.querySelectorAll(
                '#ageList input[type="checkbox"]:checked'
            ),
        ].map((cb) => cb.value);
        const selectedGender = [
            ...document.querySelectorAll(
                '#genderList input[type="checkbox"]:checked'
            ),
        ].map((cb) => cb.value);

        let visibleCards = 0;

        cards.forEach(function (card) {
            const petSpecies =
                card.querySelector(".pet-species").dataset.species;
            const petBreed = card
                .querySelector(".pet-breed")
                .dataset.breed.toLowerCase();
            const petSize = card.querySelector(".pet-size").dataset.size;
            const petAge = parseInt(card.querySelector(".pet-age").dataset.age);
            const petSex = card.querySelector(".pet-sex").dataset.sex;

            const matchesSpecies =
                selectedSpecies.length === 0 ||
                selectedSpecies.includes(petSpecies);
            const matchesBreeds =
                selectedBreeds.length === 0 ||
                selectedBreeds.some((breed) => petBreed.includes(breed));
            const matchesSizes =
                selectedSizes.length === 0 || selectedSizes.includes(petSize);
            const matchesAges =
                selectedAges.length === 0 ||
                selectedAges.some((age) => {
                    if (age === "0-1") return petAge <= 1;
                    if (age === "1-3") return petAge > 1 && petAge <= 3;
                    if (age === "3-5") return petAge > 3 && petAge <= 5;
                    if (age === "5+") return petAge > 5;
                    return false;
                });
            const matchesGender =
                selectedGender.length === 0 || selectedGender.includes(petSex);

            if (
                matchesSpecies &&
                matchesBreeds &&
                matchesSizes &&
                matchesAges &&
                matchesGender
            ) {
                card.style.display = "flex";
                visibleCards++;
            } else {
                card.style.display = "none";
            }
        });
    });
});
