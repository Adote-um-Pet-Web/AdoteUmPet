document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('searchInp');
    const searchIcon = document.getElementById('searchIcon');
    const cardsContainer = document.getElementById('cards');
    const cards = cardsContainer.querySelectorAll('.card');

    function filterCards() {
        const searchText = searchInput.value.toLowerCase();
        let visibleCards = 0;

        cards.forEach(function(card) {
            const petName = card.querySelector('.pet-name').textContent.toLowerCase();
            const petBreed = card.querySelector('.pet-breed').textContent.toLowerCase();

            if (petName.includes(searchText) || petBreed.includes(searchText)) {
                card.style.display = 'flex';
                visibleCards++;
            } else {
                card.style.display = 'none';
            }
        });
    }

    searchInput.addEventListener('keypress', function(event) {
        if (event.key === 'Enter') {
            event.preventDefault();
            filterCards();
        }
    });

    searchIcon.addEventListener('click', function() {
        filterCards();
    });
});
