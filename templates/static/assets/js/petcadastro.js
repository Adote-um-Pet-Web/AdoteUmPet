document.addEventListener("DOMContentLoaded", function () {
    const profilePetInput = document.getElementById("profilePet");
    const mainPhotoPreview = document.getElementById("main-photo-preview");

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

    const extraPhotoInputs = [
        document.getElementById("image_pet_datail1"),
        document.getElementById("image_pet_datail2"),
        document.getElementById("image_pet_datail3")
    ];

    const extraPhotoPreviews = [
        document.getElementById("extra-photo-preview-1"),
        document.getElementById("extra-photo-preview-2"),
        document.getElementById("extra-photo-preview-3")
    ];

    const ibtns = [
        document.getElementById("ibtn1"),
        document.getElementById("ibtn2"),
        document.getElementById("ibtn3")
    ];

    extraPhotoInputs.forEach((input, index) => {
        input.addEventListener("change", function () {
            const file = input.files[0];
            const preview = extraPhotoPreviews[index];
            const ibtn = ibtns[index];
            if (file) {
                const reader = new FileReader();
                reader.onload = function (e) {
                    preview.style.backgroundImage = `url(${e.target.result})`;
                    preview.style.backgroundSize = "cover";
                    preview.style.backgroundPosition = "center";
                    ibtn.style.display = "none";
                };
                reader.readAsDataURL(file);
            }
        });
    });
});