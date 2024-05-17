

const storedData = localStorage.getItem("usuarios");

if (storedData) {
    const usuario = JSON.parse(storedData);
    document.querySelector("#entrar").style.display = "none";
    document.querySelector("#avatar").style.display = "block";
    document.querySelector("#usuarioName").innerHTML = usuario.nome;
    var avatarImg = document.getElementById("avatarImg");
    avatarImg.src = usuario.foto;
}

document.querySelector("#avatar").addEventListener("click", function () {
    const userNav = document.getElementById("userNav");
    if (userNav.style.display === "none") {
        userNav.style.display = "flex";
    } else {
        userNav.style.display = "none";
    }
});

document.querySelector("#changeProfile").addEventListener("click", function () {
    window.location.href = "static/html/formulario/login.html";
});

document.querySelector("#filtro").addEventListener("click", function () {
    var navbar = document.querySelector(".navbar");
    var arrow = document.querySelector("#arrow");

    var computedStyle = window.getComputedStyle(navbar);
    var display = computedStyle.getPropertyValue("display");

    if (display === "none") {
        navbar.style.display = "block";
        arrow.innerHTML = "&#x25B4;";
    } else if (display === "block") {
        navbar.style.display = "none";
        arrow.innerHTML = "&#x25BE;";
    }
});

document.querySelector("#filtroM").addEventListener("click", function () {
    var navbarm = document.querySelector(".navbar");
    var arrowm = document.querySelector("#arrow");

    var computedStyle = window.getComputedStyle(navbarm);
    var display = computedStyle.getPropertyValue("display");

    if (display === "none") {
        navbarm.style.display = "block";
        arrowm.innerHTML = "&#x25B4;";
    } else {
        navbarm.style.display = "none";
        arrowm.innerHTML = "&#x25BE;";
    }
});

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
