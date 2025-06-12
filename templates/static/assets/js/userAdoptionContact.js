function downloadImage() {
    const container = document.querySelector("#contact-container");
    const originalWidth = container.style.width;
    const originalPadding = container.style.padding;
    
    container.style.width = "900px";
    container.style.padding = "3rem";
    
    const profileImages = container.querySelectorAll('.profile-image');
    profileImages.forEach(img => {
        img.style.width = "140px";
        img.style.height = "140px";
    });
    
    html2canvas(container, {
        scale: 3, 
        useCORS: true,
        logging: false,
        windowWidth: 900,
        windowHeight: container.scrollHeight
    }).then((canvas) => {
        container.style.width = originalWidth;
        container.style.padding = originalPadding;
        profileImages.forEach(img => {
            img.style.width = "";
            img.style.height = "";
        });
        
        let link = document.createElement("a");
        link.href = canvas.toDataURL("image/png");
        link.download = "contato_para_adocao.png";
        link.click();
    }).catch(error => {
        console.error("Erro ao gerar imagem:", error);
        container.style.width = originalWidth;
        container.style.padding = originalPadding;
        profileImages.forEach(img => {
            img.style.width = "";
            img.style.height = "";
        });
    });
}