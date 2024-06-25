const profilePetInput = document.getElementById("profilePet");
const mainPhotoPreview = document.getElementById("main-photo-preview");
const mainPhotoPreviewImg = document.getElementById("main-photo-preview-img");

profilePetInput.addEventListener("change", function () {
    const file = this.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function () {
            mainPhotoPreviewImg.src = reader.result;
            mainPhotoPreviewImg.style.display = "block";
            ibtn.style.display = "none";
        };
        reader.readAsDataURL(file);
    } else {
        mainPhotoPreviewImg.src = "#";
        mainPhotoPreviewImg.style.display = "none";
        ibtn.style.display = "block";
    }
});

const imagePetDatail1Input = document.getElementById("image_pet_datail1");
const extraPhotoPreview1 = document.getElementById("extra-photo-preview-1");
const extraPhotoPreviewImg1 = document.getElementById("extra-photo-preview-img-1");

imagePetDatail1Input.addEventListener("change", function () {
    const file = this.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function () {
            extraPhotoPreviewImg1.src = reader.result;
            extraPhotoPreviewImg1.style.display = "block";
            ibtn1.style.display = "none";
        };
        reader.readAsDataURL(file);
    } else {
        extraPhotoPreviewImg1.src = "#";
        extraPhotoPreviewImg1.style.display = "none";
        ibtn1.style.display = "block";
    }
});

const imagePetDatail2Input = document.getElementById("image_pet_datail2");
const extraPhotoPreview2 = document.getElementById("extra-photo-preview-2");
const extraPhotoPreviewImg2 = document.getElementById("extra-photo-preview-img-2");

imagePetDatail2Input.addEventListener("change", function () {
    const file = this.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function () {
            extraPhotoPreviewImg2.src = reader.result;
            extraPhotoPreviewImg2.style.display = "block";
            ibtn2.style.display = "none";
        };
        reader.readAsDataURL(file);
    } else {
        extraPhotoPreviewImg2.src = "#";
        extraPhotoPreviewImg2.style.display = "none";
        ibtn2.style.display = "block";
    }
});

const imagePetDatail3Input = document.getElementById("image_pet_datail3");
const extraPhotoPreview3 = document.getElementById("extra-photo-preview-3");
const extraPhotoPreviewImg3 = document.getElementById("extra-photo-preview-img-3");

imagePetDatail3Input.addEventListener("change", function () {
    const file = this.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function () {
            extraPhotoPreviewImg3.src = reader.result;
            extraPhotoPreviewImg3.style.display = "block";
            ibtn3.style.display = "none";
        };
        reader.readAsDataURL(file);
    } else {
        extraPhotoPreviewImg3.src = "#";
        extraPhotoPreviewImg3.style.display = "none";
        ibtn3.style.display = "block";
    }
});