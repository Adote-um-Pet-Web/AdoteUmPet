alert("OPLE")
document.addEventListener("DOMContentLoaded", function () {
    const tabs = document.querySelectorAll("#nav-list li");
    const forms = document.querySelectorAll("#espaco_dos_formularios form");
    const formTitles = [
        "Informações básicas",
        "Informações médicas",
        "Histórico",
        "Fotos",
    ];
    const formTitleElement = document.getElementById("form-title");
    const profilePetInput = document.getElementById("profilePet");
    const mainPhotoPreview = document.getElementById("main-photo-preview");
    const addPhotoButton = document.getElementById("add-photo-button");
    const adicPhotoInput = document.getElementById("adicPhoto");
    const imageContainer = document.getElementById("imageContainer");
    const maxFiles = 3;
    let someVariable = 0;

    tabs.forEach((tab, index) => {
        tab.addEventListener("click", () => {
            tabs.forEach((t) => t.classList.remove("active"));
            forms.forEach((form) => (form.style.display = "none"));

            tab.classList.add("active");
            forms[index].style.display = "flex";
            formTitleElement.textContent = formTitles[index];
        });
    });

    profilePetInput.addEventListener("change", function () {
        const file = profilePetInput.files[0];
        const ibtn = document.getElementById("ibtn");
        if (file) {
            const reader = new FileReader();
            reader.onload = function (e) {
                mainPhotoPreview.style.backgroundImage = `url(${e.target.result})`;
                mainPhotoPreview.style.backgroundSize = "cover";
                mainPhotoPreview.style.backgroundPosition = "center";
                ibtn.style.display = "none";
            };
            reader.readAsDataURL(file);
        }
    });

    addPhotoButton.addEventListener("click", function () {
        if (imageContainer.children.length < maxFiles) {
            adicPhotoInput.click();
        } else {
            alert(`Você pode adicionar no máximo ${maxFiles} fotos.`);
        }
    });

    adicPhotoInput.addEventListener("change", function () {
        const files = Array.from(adicPhotoInput.files);
        const remainingSlots = maxFiles - imageContainer.children.length;

        if (files.length > remainingSlots) {
            alert(`Você pode adicionar no máximo ${maxFiles} fotos.`);
            adicPhotoInput.value = "";
            return;
        }

        files.forEach((file) => {
            const reader = new FileReader();
            reader.onload = function (e) {
                const img = document.createElement("img");
                img.src = e.target.result;
                img.classList.add("preview-img");
                img.id = "petPhoto" + (++someVariable);
                imageContainer.appendChild(img);
            };
            reader.readAsDataURL(file);
        });
    });
});
