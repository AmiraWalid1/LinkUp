import { getAllUsers } from "./CRUD_user.js";
document.getElementById('login-form').addEventListener('submit', async function (event)
{
    event.preventDefault();
    const username = event.target.username.value;
    const password = event.target.password.value;
    
    let users = await getAllUsers();
    let user = users.find(user => user.username === username && user.password === password);

    if (user) {
        localStorage.setItem("user", JSON.stringify(user))
        window.location.href = 'home.html';
    } else {
        console.log('User not found or incorrect credentials.');
        // Handle invalid login scenario (display error message, etc.)
    }
    
});