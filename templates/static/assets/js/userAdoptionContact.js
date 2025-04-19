    function downloadImage() {
        html2canvas(document.querySelector("#contact-container"), {
            scale: 2,
            useCORS: true,
        }).then((canvas) => {
            let link = document.createElement("a");
            link.href = canvas.toDataURL("image/png");
            link.download = "informacoesDeContato.png";
            link.click();
        });
    }
