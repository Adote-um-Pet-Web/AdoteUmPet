    const form = document.getElementById('form1');
    const submitButton = document.getElementById('submit');
    const inputs = form.querySelectorAll('input, select');

    function checkFormValidity() {
        let allFieldsFilled = true;

        inputs.forEach(input => {
            if (input.value.trim() === '' || input.value === '0') {
                allFieldsFilled = false;
            }
        });

        if (allFieldsFilled) {
            submitButton.disabled = false;
            submitButton.classList.remove('disabled-button');
        } else {
            submitButton.disabled = true;
            submitButton.classList.add('disabled-button');
        }
    }

    inputs.forEach(input => {
        input.addEventListener('input', checkFormValidity);
    });

    window.addEventListener('load', checkFormValidity);
