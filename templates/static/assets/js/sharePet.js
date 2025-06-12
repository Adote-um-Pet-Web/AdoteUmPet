const canvas = document.getElementById("canvas");
const shareText = "abcde";

document.getElementById("download").addEventListener("click", function () {
    html2canvas(canvas).then(function (canvas) {
        const link = document.createElement("a");
        link.href = canvas.toDataURL("image/png");
        link.download = "imagem_instagram.png";
        link.click();
    });
    if (typeof confetti === "function") {
        confetti({
            particleCount: 100,
            spread: 70,
            origin: { y: 0.6 },
        });
    }
});

document.getElementById("share").addEventListener("click", function () {
    html2canvas(canvas).then(function (canvas) {
        canvas.toBlob(function (blob) {
            const filesArray = [
                new File([blob], "imagem.png", { type: "image/png" }),
            ];
            if (
                navigator.canShare &&
                navigator.canShare({ files: filesArray })
            ) {
                navigator
                    .share({
                        files: filesArray,
                        title: "Compartilhar Imagem",
                        text: "Confira esta imagem!" + shareText,
                    })
                    .then(() => {
                        alert("Compartilhamento bem-sucedido");
                    })
                    .catch((error) => {
                        console.error("Erro ao compartilhar:", error);
                        alert("Erro no compartilhamento");
                    });
            } else {
                alert(
                    "O compartilhamento direto não é suportado neste navegador."
                );
            }
        }, "image/png");
    });
});
