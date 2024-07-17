import { getUser } from "./CRUD_user.js";
import { postPost } from "./CRUD-post.js";
let user = JSON.parse(localStorage.getItem('user'));
let user_name = document.querySelector(".user-name");
let post_img = document.querySelector(".post-pic");

// console.log(user);
user_name.innerHTML = user.first_name + ' ' + user.last_name + user_name.innerHTML;
post_img.src = user.photo || "../static/styles/imgs/me.png";


document.querySelector(".Posts").addEventListener("click", async function (event){
    event.preventDefault();
    
    const content = document.querySelector('#postContent').value;

    await getUser(user.username, user.password);
    user = JSON.parse(localStorage.getItem('user'));
    // console.log(user);

    await postPost(user, content);
});