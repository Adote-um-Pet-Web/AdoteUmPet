document.addEventListener("DOMContentLoaded", () => {
    const colorButtons = document.querySelectorAll(".color-option");
    const themeButtons = document.querySelectorAll(".theme-option");
    const applyColorButton = document.querySelectorAll(
        "section.configSection button"
    )[0];
    const applyThemeButton = document.querySelectorAll(
        "section.configSection button"
    )[1];

    const defaultColor = "padrao";
    const defaultTheme = "auto";

    let selectedColor = localStorage.getItem("selectedColor") || defaultColor;
    let selectedTheme = localStorage.getItem("selectedTheme") || defaultTheme;

    document.body.setAttribute("data-color", selectedColor);
    if (selectedTheme === "auto") {
        const prefersDarkScheme = window.matchMedia(
            "(prefers-color-scheme: dark)"
        ).matches;
        document.body.setAttribute(
            "data-theme",
            prefersDarkScheme ? "dark" : "light"
        );
    } else {
        document.body.setAttribute("data-theme", selectedTheme);
    }

    colorButtons.forEach((button) => {
        if (button.textContent.toLowerCase() === getColorName(selectedColor)) {
            button.classList.add("selected");
        }
    });

    themeButtons.forEach((button) => {
        if (button.textContent.toLowerCase() === getThemeName(selectedTheme)) {
            button.classList.add("selected");
        }
    });

    colorButtons.forEach((button) => {
        button.addEventListener("click", () => {
            colorButtons.forEach((btn) => btn.classList.remove("selected"));
            button.classList.add("selected");
            selectedColor = button.getAttribute("data-color");
            localStorage.setItem("selectedColor", selectedColor);
        });
    });

    themeButtons.forEach((button) => {
        button.addEventListener("click", () => {
            themeButtons.forEach((btn) => btn.classList.remove("selected"));
            button.classList.add("selected");
            selectedTheme = button.getAttribute("data-theme");
            localStorage.setItem("selectedTheme", selectedTheme);
        });
    });

    applyColorButton.addEventListener("click", () => {
        if (selectedColor) {
            document.body.setAttribute("data-color", selectedColor);
        }
    });

    applyThemeButton.addEventListener("click", () => {
        if (selectedTheme) {
            if (selectedTheme === "auto") {
                const prefersDarkScheme = window.matchMedia(
                    "(prefers-color-scheme: dark)"
                ).matches;
                document.body.setAttribute(
                    "data-theme",
                    prefersDarkScheme ? "dark" : "light"
                );
            } else {
                document.body.setAttribute("data-theme", selectedTheme);
            }
        }
    });
});

function capitalizeFirstLetter(string) {
    return string.charAt(0).toUpperCase() + string.slice(1);
}

function getColorName(color) {
    if (color === "padrao") return "amarelo";
    if (color === "invertido") return "azul";
    return color;
}

function getThemeName(theme) {
    if (theme === "light") return "claro";
    if (theme === "dark") return "escuro";
    return "automático";
}
