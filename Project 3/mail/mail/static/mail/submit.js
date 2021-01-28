document.addEventListener('DOMContentLoaded', () => {
    const form = document.querySelector('form');
    form.onsubmit = function (event) {
        event.preventDefault();
        const recipients = document.querySelector('#compose-recipients').value;
        const subject = document.querySelector('#compose-subject').value;
        const body = document.querySelector('#compose-body').value;
        if (from.length == 0 && recipients.length == 0) return;
        fetch('/emails', {
            method: 'POST',
            body: JSON.stringify({
                recipients: recipients,
                subject: subject,
                body: body
            })
        })
        .then(response => response.json())
        .then(result => {
            console.log(result);
            load_mailbox('sent');
        });
    }
});