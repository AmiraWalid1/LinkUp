async function getComments(){
    let commentsResponse  = await fetch('http://localhost:5000/api/v1/<user_id>/comments');
    let comments = await likesResponse.json();

    for(let comment of comments){

        let postResponse = await fetch(`http://localhost:5000/api/v1/posts/${comment.post_id}`);
        let post = await postResponse.json();

        let userResponse = await fetch(`http://localhost:5000/api/v1/users/${post.user_id}`);
        let user = await userResponse.json()
        console.log(user);
        document.querySelector('.posts-container').innerHTML += getHTML(user, comment);
    }
}