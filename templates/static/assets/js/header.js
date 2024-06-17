const menuIconMobile = document.getElementById("menuIconMobile");
const moreItens = document.getElementById("moreItens");
const avatar = document.getElementById("avatar");
const userNav = document.getElementById("userNav");

menuIconMobile.addEventListener("click", function () {
  toggleMoreItens();
});

avatar.addEventListener("click", function () {
  toggleUserNav();
});

function toggleMoreItens() {
  if (moreItens.style.display === "none") {
    moreItens.style.display = "flex";
    moreItens.style.animation = "slideDown 0.3s ease forwards";
  } else {
    moreItens.style.animation = "slideUp 0.3s ease forwards";
    setTimeout(() => {
      moreItens.style.display = "none";
    }, 300);
  }
}

function toggleUserNav() {
  if (userNav.style.display === "none") {
    userNav.style.display = "flex";
    userNav.style.animation = "slideDown 0.3s ease forwards";
  } else {
    userNav.style.animation = "slideUp 0.3s ease forwards";
    setTimeout(() => {
      userNav.style.display = "none";
    }, 300);
  }
}

const observer = new MutationObserver(function(mutations) {
  mutations.forEach(function(mutation) {
    if (mutation.attributeName === "style") {
      adjustUserNavPosition();
    }
  });
});

observer.observe(moreItens, {
  attributes: true,
  attributeFilter: ["style"]
});

function adjustUserNavPosition() {
  if (moreItens.style.display === "flex") {
    userNav.style.top = "7.1rem";
  } else {
    userNav.style.top = "4.23rem";
  }
}