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
        userNav.style.animation = "slideDown 0.3s ease forwards";
    } else {
        userNav.style.animation = "slideUp 0.3s ease forwards";
        setTimeout(() =>{
            userNav.style.display = "none";
        }, 300);
    }
});


