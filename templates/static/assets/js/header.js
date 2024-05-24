document
    .getElementById("menuIconMobile")
    .addEventListener("click", function () {
        const moreItens = document.getElementById("moreItens");
        if (moreItens.style.display == "none") {
            moreItens.style.display = "flex";
        } else {
            moreItens.style.display = "none";
        }
    });
document.querySelector("#avatar").addEventListener("click", function () {
    const userNav = document.getElementById("userNav");
    if (userNav.style.display === "none") {
        userNav.style.display = "flex";
    } else {
        userNav.style.display = "none";
    }
});


