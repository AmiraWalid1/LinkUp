export async function postPost(user, content){
    try {
        let response = await fetch(`http://localhost:5000/api/v1/users/${user.id}/posts`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({content}),
        });
    
        if (!response.ok) {
            const errorText = await response.text();  // Read response body as text
            throw new Error(`HTTP error! status: ${response.status}, message: ${errorText}`);
        }
    
        let data = await response.json();

        // Redirect to the login page after successful sign-up
        window.location.href = 'home.html';
    } catch (error) {
        console.error('Error:', error);
    }
}