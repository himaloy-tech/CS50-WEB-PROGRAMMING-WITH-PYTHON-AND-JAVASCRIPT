document.addEventListener('DOMContentLoaded', function () {
    const submit_button = document.querySelector('#submit_button');
    submit_button.addEventListener('click', function (event) {
        const recipeints = document.querySelector('#compose-recipients').value;
        const subject = document.querySelector('#compose-subject').value;
        const body = document.querySelector('#compose-body').value;
        fetch('/emails', {
            method: 'POST',
            body: JSON.stringify({
                recipients: recipeints,
                subject: subject,
                body: body
            })
        })
            .then(response => response.json())
            .then(result => {
                console.log(result);
                if (result.status == 400) {
                    message.style.display = 'block';
                    message.innerHTML = result;
                } else {
                    load_mailbox('sent');
                }
            });
    });
});