export async function postUser(user) {
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
        window.location.href = 'profile.html';
    } catch (error) {
        console.error('Error:', error);
    }
    
}

export async function putUser(user) {
    try {
        let response = await fetch(`http://localhost:5000/api/v1/users/${user.id}`, {
            method: 'PUT',
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
        window.location.href = 'profile.html';
    } catch (error) {
        console.error('Error:', error);
    }
    
}

export async function getUser(username, password) {
    try{
        const response = await fetch('http://localhost:5000/api/v1/users');
        if (!response.ok) {
            const errorText = await response.text();  // Read response body as text
            throw new Error(`HTTP error! status: ${response.status}, message: ${errorText}`);
        }

        let data = await response.json();
        // console.log(data);
        const user = data.find(user => user.username === username && user.password === password);

        if (user) {
            // Redirect to home.html on successful login
            localStorage.setItem("user", JSON.stringify(user))
        } else {
            console.log('User not found or incorrect credentials.');
            // Handle invalid login scenario (display error message, etc.)
        }
    } catch (error) {
        console.error('Error:', error);
    }
    
};





