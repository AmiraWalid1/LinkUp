document.getElementById('login-form').addEventListener('submit', async function (event)
{
    event.preventDefault();
    const name = event.target.username.value;
    const password = event.target.password.value;
    try{
        const response = await fetch('http://localhost:5000/api/v1/users');
        if (!response.ok) {
            const errorText = await response.text();  // Read response body as text
            throw new Error(`HTTP error! status: ${response.status}, message: ${errorText}`);
        }

        let data = await response.json();
        // console.log(data);
        const user = data.find(user => user.name === name && user.password === password);

        if (user) {
            // Redirect to home.html on successful login
            window.location.href = new URL(window.location.origin + '/web_flask/templates/home.html');
        } else {
            console.log('User not found or incorrect credentials.');
            // Handle invalid login scenario (display error message, etc.)
        }
    } catch (error) {
        console.error('Error:', error);
    }
});