document
    .getElementById("changePhoto")
    .addEventListener("change", function (event) {
        const reader = new FileReader();
        reader.onload = function () {
            const output = document.getElementById("profileImage");
            output.src = reader.result;
        };
        reader.readAsDataURL(event.target.files[0]);
    });
console.log("alllalllalalaallalalalaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa");