async function getComments(){
    let commentsResponse  = await fetch('http://localhost:5000/api/v1/<user_id>/comments');
    let comments = await likesResponse.json();

    for(let comment of comments){
        let userResponse = await fetch(`http://localhost:5000/api/v1/posts/${comment.user_id}`);
        let user = await userResponse.json();

        let postResponse = await fetch(`http://localhost:5000/api/v1/posts/${comment.post_id}`);
        let post = await postResponse.json();

        let authorResponse = await fetch(`http://localhost:5000/api/v1/users/${post.user_id}`);
        let author = await authorResponse.json()
        
        document.querySelector('.posts-container').innerHTML += getHTML(post, author, user, comment);
    }
}
getComments();
