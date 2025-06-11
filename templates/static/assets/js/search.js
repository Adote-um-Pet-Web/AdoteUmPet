document.addEventListener("DOMContentLoaded", function () {
    const searchInput = document.getElementById("searchInp");
    const searchIcon = document.getElementById("searchIcon");
    const cardsContainer = document.getElementById("cards");

    function filterCards() {
        const searchText = searchInput.value.trim().toLowerCase();
        const cards = cardsContainer.querySelectorAll(".card");
        let hasVisibleCards = false;

        cards.forEach(function (card) {
            const petName = card
                .querySelector(".pet-name")
                .textContent.toLowerCase();
            const petBreed = card
                .querySelector(".pet-breed")
                .textContent.toLowerCase();
            const petSpecies = card
                .querySelector(".pet-species")
                .textContent.toLowerCase();
            const petOwner =
                card.querySelector(".pet-owner")?.textContent.toLowerCase() ||
                "";

            if (
                petName.includes(searchText) ||
                petBreed.includes(searchText) ||
                petSpecies.includes(searchText) ||
                petOwner.includes(searchText)
            ) {
                card.style.display = "flex";
                hasVisibleCards = true;
            } else {
                card.style.display = "none";
            }
        });

        const noResultsMessage = document.querySelector(".no-results-message");
        if (noResultsMessage) {
            noResultsMessage.style.display = hasVisibleCards ? "none" : "block";
        }
    }

    searchInput.addEventListener("input", function () {
        filterCards();
    });

    searchInput.addEventListener("keypress", function (event) {
        if (event.key === "Enter") {
            event.preventDefault();
            filterCards();
        }
    });

    searchIcon.addEventListener("click", function () {
        filterCards();
    });

    searchIcon.addEventListener("mousedown", function (e) {
        e.preventDefault();
        searchInput.focus();
    });
});
