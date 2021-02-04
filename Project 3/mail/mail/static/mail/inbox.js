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
        emails_view.innerHTML = '';
        emails.forEach(email => {
          const div_element = document.createElement('div');
          if(email.read){
            div_element.className = `alert alert-dark`;
          } else{
            div_element.className = `alert alert-light`;
          }
          div_element.style = "border:solid grey 1px";
          const element = `<h4 class="alert-heading">${email.subject}</h4>
          <p>${email.sender}</p>
          <hr>
          <p class="mb-0">${email.timestamp}</p>`;
          div_element.innerHTML = element;
          div_element.addEventListener('click', () => detail(email.id, mailbox));
          emails_view.append(div_element);
        });
      }
    })
  }
  
function detail(id, mailbox){
  fetch(`/emails/${id}`)
  .then(response => response.json())
  .then(details => {
    const emails_view = document.querySelector('#emails-view');
    emails_view.innerHTML = '';
    document.querySelector('h3').innerHTML = '';
    const mail = document.createElement('div');
    mail.className = 'jumbotron';
    const text = `<h3>Subject : ${details.subject}</h3>
    <p class="lead">Body : ${details.body}</p>
    <hr class="my-4">
    <p>Sender : ${details.sender}</p>
    <p>Recipients : ${details.recipients}</p>
    <p>Timestamp : ${details.timestamp}</p>`;
    mail.innerHTML = text;
    emails_view.append(mail);
    const button = document.createElement('button');
    if(details.archived){
      button.className = 'btn btn-danger';
      button.innerHTML = 'Unarchive';
    } else{
      button.className = 'btn btn-primary';
      button.innerHTML = 'Archive';
    }
    button.addEventListener('click', () => {
      archive(id, details.archived);
      window.location.reload(true);
    });
    if(mailbox != "sent"){
      emails_view.appendChild(button);
    }
    fetch(`/emails/${id}`, {
      method: 'PUT',
      body: JSON.stringify({
          read:true
      })
    })
  })
  .catch(error => {
    console.log(error);
  })
}

function archive(id, value){
  fetch(`/emails/${id}`, {
    method:"PUT",
    body:JSON.stringify({
      archived: !value
    }),
  });
}












