document.getElementById('signup-form').addEventListener('submit', async function (event) {
    event.preventDefault();
    const username = event.target.username.value;
    const email = event.target.email.value;
    const password = event.target.password.value;
    let user = {username, email, password}
    localStorage.setItem('user', JSON.stringify(user));

    let url = new URL(window.location.origin + '/web_flask/templates/EditProfile.html');
    window.location.href = url;
});

