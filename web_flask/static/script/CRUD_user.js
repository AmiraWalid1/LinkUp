async function postUser(user) {
    try {
        let response = await fetch('http://localhost:5000/api/v1/users', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(user),
        });
    
        if (!response.ok) {
            const errorText = await response.text();  // Read response body as text
            throw new Error(`HTTP error! status: ${response.status}, message: ${errorText}`);
        }
    
        let data = await response.json();
        // console.log(data);
    
        // Redirect to the login page after successful sign-up
        url = new URL(window.location.origin + '/web_flask/templates/login.html');
        window.location.href = url;
    } catch (error) {
        console.error('Error:', error);
    }
    
}
