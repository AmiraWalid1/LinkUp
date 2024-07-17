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
function getHTML(post, author, user, comment) {
    return `
        <div class="post-container">
            <div class="profileAndUser">
                <img class="post-pic" src="../static/styles/imgs/me.png" alt="profile Pic">
                <div class="userAndOline">
                    <h2 class="user-name" style="height: 29px; margin-top: 62px;">${author.first_name + ' ' + author.last_name}</h2>
                    <p style="height: 16px; margin-top: 0px;"> 4m <img src="../static/styles/imgs/earth.png" alt="bell"
                            height="12px" style="margin-top: 5px;"></p>
                </div>

            </div>

            <div class="post-text">
                <p style="white-space:wrap; margin-left: 45px; margin-bottom: 25px; font-size: 18px;">${post.content}
                </p>

            </div>

            <div class="post-options-formula">
                <a href="#" class="options">
                    <img src="../static/styles/imgs/like.png" alt="Media" height="20px" style="margin-right: 10px;">
                    <p> Like</p>
                </a>
                <a href="comments.html" class="options">
                    <img src="../static/styles/imgs/comment.png" alt="Event" height="20px" style="margin-right: 10px;">
                    <p> Comment</p>
                </a>
                <a href="#" class="options">
                    <img src="../static/styles/imgs/share.png" alt="Event" height="20px" style="margin-right: 10px;">
                    <p> Share</p>
                </a>
            </div>

            <div class="comment">
                <img src=".././static/styles/imgs/me.png" alt="" width="70px" height="70px" border: .5px solid grey;
                style="border-radius: 50%; border: 0.5px solid grey; margin-top: 24px; margin-right: 15px;">
                <div class="comment-container">
                    <div class="user-time">
                        <p class="comment-name">${user.first_name + ' ' + user.last_name}</p>
                        <p class="comment-time">1m</p>
                    </div>

                    <p class="comment-text">${comment.content}</p>

                </div>
            </div>
        </div>

    `

}