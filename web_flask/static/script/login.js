import { getUser } from "./CRUD_user.js";
document.getElementById('login-form').addEventListener('submit', async function (event)
{
    event.preventDefault();
    const username = event.target.username.value;
    const password = event.target.password.value;
    
    await getUser(username, password);
    window.location.href = 'home.html';
});