import { postPost } from "./CRUD-post.js";
let user = JSON.parse(localStorage.getItem('user'));
let user_name = document.querySelector(".user-name");
let user_img = document.querySelector(".post-pic");

user_name.innerHTML = user.first_name + ' ' + user.last_name + user_name.innerHTML;
user_img.src = user.photo || "../static/styles/imgs/me.png";

document.querySelector(".Posts").addEventListener("click", async function (event) {
    event.preventDefault();

    const content = document.querySelector('#postContent').value;
    await postPost(user, {content});
});
