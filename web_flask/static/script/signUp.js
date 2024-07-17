document.getElementById('signup-form').addEventListener('submit', async function (event) {
    event.preventDefault();
    const username = event.target.username.value;
    const email = event.target.email.value;
    const password = event.target.password.value;
    let user = {username, email, password}
    localStorage.setItem('user', JSON.stringify(user));

    window.location.href = 'edit-profile.html';
});

