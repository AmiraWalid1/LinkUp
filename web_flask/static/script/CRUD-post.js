export async function postPost(user, post){
    try {
        let response = await fetch(`http://localhost:5000/api/v1/users/${user.id}/posts`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(post),
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

export async function getAllPosts(){
    // get all posts
    try {
        let response = await fetch('http://localhost:5000/api/v1/posts');
    
        if (!response.ok) {
            const errorText = await response.text();  // Read response body as text
            throw new Error(`HTTP error! status: ${response.status}, message: ${errorText}`);
        }
    
        let data = await response.json();

        return data;
    } catch (error) {
        console.error('Error:', error);
    }
}