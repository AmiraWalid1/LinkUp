async function getLikes(){
    let likesResponse  = await fetch('http://localhost:5000/api/v1/<user_id>/likes');
    let likes = await likesResponse.json();
}

for(let like of likes){
    console.log(like.user_id);
    let userResponse = await fetch(`http://localhost:5000/api/v1/users/${like.user_id}`);
    let user = await userResponse.json()
    console.log(user);
    document.querySelector('.posts-container').innerHTML += getHTML(like, user);
}

