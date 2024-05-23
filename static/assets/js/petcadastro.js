document.addEventListener("DOMContentLoaded", function() {
    const navList = document.getElementById('nav-list');
    const formHeader = document.querySelector('#espaco_dos_formularios h3');

    navList.addEventListener('click', function(event) {
        if (event.target.tagName === 'LI') {
            const selectedContent = event.target.getAttribute('data-content');
            formHeader.textContent = selectedContent;

            const allNavItems = navList.querySelectorAll('li');
            allNavItems.forEach(function(navItem) {
                navItem.classList.remove('active');
            });

            event.target.classList.add('active');
        }
    });
});