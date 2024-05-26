window.alert("oiiiiiiiii");

const fileInput = document.getElementById("fileInput");
const previewContainer = document.getElementById("preview-container");
const preview = document.getElementById("preview");
const iconPlaceholder = document.getElementById("iconPlaceholder");

fileInput.addEventListener("change", function () {
    const file = this.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function () {
            preview.src = reader.result;
            preview.style.display = "block";
            iconPlaceholder.style.display = "none";
        };
        reader.readAsDataURL(file);
    } else {
        preview.src = "#";
        preview.style.display = "none";
        iconPlaceholder.style.display = "block";
    }
});

const previewContainerM = document.getElementById("preview-containerM");
const previewM = document.getElementById("previewM");
const iconPlaceholderM = document.getElementById("iconPlaceholderM");

fileInput.addEventListener("change", function () {
    const fileM = this.files[0];
    if (fileM) {
        const readerM = new FileReader();
        readerM.onload = function () {
            previewM.src = readerM.result;
            previewM.style.display = "block";
            iconPlaceholderM.style.display = "none";
        };
        readerM.readAsDataURL(fileM);
    } else {
        previewM.src = "#";
        previewM.style.display = "none";
        iconPlaceholderM.style.display = "block";
    }
});