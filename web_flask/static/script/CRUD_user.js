export async function postUser(user) {
    // post new user
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
    
        return data;
    } catch (error) {
        console.error('Error:', error);
    }
    
}

export async function putUser(user) {
    // update data of user
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
        return data;
    } catch (error) {
        console.error('Error:', error);
    }
    
}

export async function getAllUsers(username, password) {
    // return user with spacific name and password
    try{
        const response = await fetch('http://localhost:5000/api/v1/users');
        if (!response.ok) {
            const errorText = await response.text();  // Read response body as text
            throw new Error(`HTTP error! status: ${response.status}, message: ${errorText}`);
        }

        let data = await response.json();
        // console.log(data);
       return data;
    } catch (error) {
        console.error('Error:', error);
    }
    
};





