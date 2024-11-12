// static/confirm_empty_field.js
document.addEventListener('DOMContentLoaded', function() {
    // Disable submit form on Enter
    document.addEventListener(`keypress`, (event) => {
        if (event.target.nodeName == 'INPUT') {
            if (event.key === `Enter`) {
                event.preventDefault();
            }
            return true;
        }
    });
    
    // Add prompt when Personal ID Number is empty
    const submitButtons = document.querySelectorAll('input[type="submit"]');

    const submitCallback = (event) => {
        const personalIdField = document.getElementById('id_personal_number');

        // If the field is empty, show a confirmation prompt
        if (personalIdField && personalIdField.value.trim() === '') {
            const confirmLeaveEmpty = confirm("The Personal ID Number field is empty. Are you sure you want to leave this field empty?");
            if (!confirmLeaveEmpty) {
                event.preventDefault();
            }
        }
    };

    submitButtons.forEach((button) => {
        button.addEventListener('click', submitCallback);
    });
});