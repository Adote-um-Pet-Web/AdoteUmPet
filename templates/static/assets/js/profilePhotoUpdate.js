document.addEventListener("DOMContentLoaded", function () {
    const fileInput = document.getElementById("changePhoto");
    const imagePreview = document.getElementById("profileImagePreview");

    if (fileInput && imagePreview) {
        fileInput.addEventListener("change", function (event) {
            const file = event.target.files[0];

            if (!file) return;

            const validTypes = ["image/jpeg", "image/png", "image/jpg"];
            if (!validTypes.includes(file.type)) {
                alert("Por favor, selecione uma imagem no formato JPG ou PNG.");
                return;
            }

            if (file.size > 5 * 1024 * 1024) {
                alert(
                    "A imagem é muito grande. O tamanho máximo permitido é 5MB."
                );
                return;
            }

            const reader = new FileReader();
            reader.onload = function (e) {
                imagePreview.src = e.target.result;
            };
            reader.readAsDataURL(file);
        });
    }
});
