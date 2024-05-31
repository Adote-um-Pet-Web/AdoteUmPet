document.addEventListener('DOMContentLoaded', () => {
    const colorButtons = document.querySelectorAll('section.configSection ul:nth-of-type(1) li');
    const themeButtons = document.querySelectorAll('section.configSection ul:nth-of-type(2) li');
    const applyColorButton = document.querySelectorAll('section.configSection button')[0];
    const applyThemeButton = document.querySelectorAll('section.configSection button')[1];

    const defaultColor = 'padrao';
    const defaultTheme = 'auto';

    let selectedColor = localStorage.getItem('selectedColor') || defaultColor;
    let selectedTheme = localStorage.getItem('selectedTheme') || defaultTheme;

    document.body.setAttribute('data-color', selectedColor);
    if (selectedTheme === 'auto') {
        const prefersDarkScheme = window.matchMedia("(prefers-color-scheme: dark)").matches;
        document.body.setAttribute('data-theme', prefersDarkScheme ? 'dark' : 'light');
    } else {
        document.body.setAttribute('data-theme', selectedTheme);
    }

    colorButtons.forEach(button => {
        if (button.textContent.toLowerCase() === getColorName(selectedColor)) {
            button.classList.add('selected');
        }
    });

    themeButtons.forEach(button => {
        if (button.textContent.toLowerCase() === getThemeName(selectedTheme)) {
            button.classList.add('selected');
        }
    });

    colorButtons.forEach(button => {
        button.addEventListener('click', () => {
            colorButtons.forEach(btn => btn.classList.remove('selected'));
            button.classList.add('selected');
            const colorText = button.textContent.toLowerCase();
            if (colorText === 'amarelo') {
                selectedColor = 'padrao';
            } else if (colorText === 'azul') {
                selectedColor = 'invertido';
            } else if (colorText === 'laranja') {
                selectedColor = 'laranja';
            }
            localStorage.setItem('selectedColor', selectedColor);
        });
    });

    themeButtons.forEach(button => {
        button.addEventListener('click', () => {
            themeButtons.forEach(btn => btn.classList.remove('selected'));
            button.classList.add('selected');
            const themeText = button.textContent.toLowerCase();
            if (themeText === 'claro') {
                selectedTheme = 'light';
            } else if (themeText === 'escuro') {
                selectedTheme = 'dark';
            } else if (themeText === 'automático') {
                selectedTheme = 'auto';
            }
            localStorage.setItem('selectedTheme', selectedTheme);
        });
    });

    applyColorButton.addEventListener('click', () => {
        if (selectedColor) {
            document.body.setAttribute('data-color', selectedColor);
        }
    });

    applyThemeButton.addEventListener('click', () => {
        if (selectedTheme) {
            if (selectedTheme === 'auto') {
                const prefersDarkScheme = window.matchMedia("(prefers-color-scheme: dark)").matches;
                document.body.setAttribute('data-theme', prefersDarkScheme ? 'dark' : 'light');
            } else {
                document.body.setAttribute('data-theme', selectedTheme);
            }
        }
    });
});

function capitalizeFirstLetter(string) {
    return string.charAt(0).toUpperCase() + string.slice(1);
}

function getColorName(color) {
    if (color === 'padrao') return 'amarelo';
    if (color === 'invertido') return 'azul';
    return color;
}

function getThemeName(theme) {
    if (theme === 'light') return 'claro';
    if (theme === 'dark') return 'escuro';
    return 'automático';
}
