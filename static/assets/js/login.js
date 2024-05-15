// change page login => registro
const criarPageBtn = document.querySelector("#criarConta");
const entrarPageBtn = document.querySelector("#entrarBtn");
const login = document.querySelector("#login");
const registro = document.querySelector("#registro");

criarPageBtn.addEventListener("click", function () {
    login.style.display = "none";
    registro.style.display = "flex";
});
entrarPageBtn.addEventListener("click", function () {
    login.style.display = "flex";
    registro.style.display = "none";
});

const confirmAvatar = document.getElementById("confirmAvatar");
const avatar = document.getElementById("avatarUrl").value;
const avataruserAreaPhotoArea = document.getElementById("userAreaPhoto");
confirmAvatar.addEventListener("click", function () {
    const img = document.createElement("img");
    img.src = avatar;
    img.classList.add("avatar-image");
    avataruserAreaPhotoArea.innerHTML = "";
    avataruserAreaPhotoArea.appendChild(img);
});

// simple login
document.getElementById("entrar").addEventListener("click", function (event) {
    event.preventDefault();

    const storedData = localStorage.getItem("usuarios");

    if (storedData) {
        const usuarios = JSON.parse(storedData);
        const email = document.getElementById("email").value;
        const senha = document.getElementById("senha").value;

        if (email === usuarios.email && senha === usuarios.senha) {
            window.location.href = "/all/index.html";
        } else {
            alert("Credenciais inválidas. Por favor, tente novamente.");
        }
    } else {
        alert(
            "Não foi possível recuperar os dados de registro. Por favor, registre-se primeiro."
        );
    }
});


// simple create accont
document
    .getElementById("cadastrar")
    .addEventListener("click", function (event) {
        event.preventDefault();
        const email = document.getElementById("email").value;
        const senha = document.getElementById("senha").value;
        const nome = document.getElementById("name").value;
        const telefone = document.getElementById("telefone").value;
        const foto = document.getElementById("avatarUrl").value;

        const usuarios = {
            email: email,
            senha: senha,
            nome: nome,
            telefone: telefone,
            foto: foto,
        };

        localStorage.setItem("usuarios", JSON.stringify(usuarios));

        document.getElementById("email").value = "";
        document.getElementById("senha").value = "";
        document.getElementById("name").value = "";
        document.getElementById("telefone").value = "";

        alert("Usuário cadastrado com sucesso!");

        const login = document.querySelector("#login");
        const registro = document.querySelector("#registro");
        login.style.display = "flex";
        registro.style.display = "none";
    });
