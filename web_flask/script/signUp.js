document.getElementById('signup-form').addEventListener('submit', async function (event) {
    event.preventDefault();
    const name = event.target.username.value;
    const email = event.target.email.value;
    const password = event.target.password.value;

    try {
        let response = await fetch('http://localhost:5000/api/v1/users', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ name, email, password }),
        });

        if (!response.ok) {
            const errorText = await response.text();  // Read response body as text
            throw new Error(`HTTP error! status: ${response.status}, message: ${errorText}`);
        }

        let data = await response.json();
        // console.log(data);

        // Redirect to the login page after successful sign-up
        const url = new URL(window.location.origin + '/web_flask/templates/login.html');
        window.location.href = url;
    } catch (error) {
        console.error('Error:', error);
    }
});
