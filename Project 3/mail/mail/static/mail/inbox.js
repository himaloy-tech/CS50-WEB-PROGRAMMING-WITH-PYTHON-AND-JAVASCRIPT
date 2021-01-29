document.addEventListener('DOMContentLoaded', function () {

  // Use buttons to toggle between views
  document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
  document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
  document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
  document.querySelector('#compose').addEventListener('click', compose_email);

  // By default, load the inbox
  load_mailbox('inbox');
});

function compose_email() {

  // Show compose view and hide other views
  document.querySelector('h3').innerHTML = "New Email";

  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('form').style.display = 'block';

  // Clear out composition fields
  document.querySelector('#compose-recipients').value = '';
  document.querySelector('#compose-subject').value = '';
  document.querySelector('#compose-body').value = '';
}

function load_mailbox(mailbox) {

  // Show the mailbox and hide other views

  const emails_view = document.querySelector('#emails-view');
  emails_view.style.display = 'block';
  document.querySelector('form').style.display = 'none';

  // Show the mailbox name
  document.querySelector('h3').innerHTML = `${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}`;
  fetch(`/emails/${mailbox}`)
    .then(response => response.json())
    .then(emails => {
      if(emails.length == 0){
        emails_view.innerHTML = '';
      } else{
        emails.forEach(email => {
          let color = 'alert-light';
          if(email.read){
            let color = 'alert-dark';
          }
          const element = `<a onclick="email_deatail(${email.id})"><div class="alert ${color}" role="alert" style="border:solid black 1px" ><h4 class="alert-heading">${email.subject}</h4>
          <p>${email.sender}</p>
          <hr>
          <p class="mb-0">${email.timestamp}</p>
          </div></a>`;
          emails_view.innerHTML = element;
        });
      }
    })
}