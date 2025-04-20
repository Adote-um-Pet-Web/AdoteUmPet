            function changeColor(variable) {
                const newColor = prompt(
                    "Digite uma nova cor (em formato hexadecimal, ex: #ffffff):"
                );
                if (newColor !== null && newColor !== "") {
                    const variableName = variable.substring(2); // Remove '--'
                    document.querySelectorAll('.color-square').forEach(function(square) {
                        if (square.getAttribute('data-color-var') === variable) {
                            square.style.backgroundColor = newColor;
                        }
                    });
                }
            }
   
function previewBanner(event, bannerId) {
    const reader = new FileReader();
    reader.onload = function () {
        const previewImg = document.getElementById(
            bannerId + "-preview-img"
        );
        previewImg.src = reader.result;
        previewImg.style.display = "block";
                };
        reader.readAsDataURL(event.target.files[0]);
}
        