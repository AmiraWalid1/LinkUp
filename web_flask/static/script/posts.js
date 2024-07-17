async function getPosts(){
    let postsResponse = await fetch('http://localhost:5000/api/v1/posts');
    let posts = await postsResponse.json();

    for(let post of posts){
        console.log(post.user_id);
        let userResponse = await fetch(`http://localhost:5000/api/v1/users/${post.user_id}`);
        let user = await userResponse.json()
        console.log(user);
        document.querySelector('.posts-container').innerHTML += getHTML(post, user);
    }

}
getPosts();
function getHTML(post, user){
    return `
    <div class="post-container">
            <div class="profileAndUser">
                <img class="post-pic" src="../static/styles/imgs/me.png" alt="profile Pic">
                <div class="userAndOline">
                    <h2 class="user-name" style="height: 29px; margin-top: 62px;">${user.first_name + ' ' + user.last_name}</h2>
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

            <div class="profileAndPost">
                <img class="profile-pic" src="../static/styles/imgs/me.png" alt="profile-pic" width="70px">

                <div class="start-comment">
                    <input class="post-input" type="text" placeholder="Add a comment" style="font-size: 16px ; width: 75%;">
                    <a href="#"><img src="../static/styles/imgs/emoji.png" alt="" height="29px"
                            style="margin-right: 24px;"></a>
                    <a href="#"></a><img src="../static/styles/imgs/folder.png" alt="" height="29px"
                        style="margin-right: 63px;"></a>
                </div>
            </div>

        </div>
    `
}