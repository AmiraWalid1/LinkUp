import { postPost } from "./CRUD-post.js";
let user = JSON.parse(localStorage.getItem('user'));
let user_name = document.querySelector(".user-name");
let user_img = document.querySelector(".post-pic");

user_name.innerHTML = user.first_name + ' ' + user.last_name + user_name.innerHTML;
user_img.src = user.photo || "../static/styles/imgs/me.png";

// document.getElementById('file').addEventListener('change', function(event) {
//     const fileInput = event.target;
//     const file = fileInput.files[0];

//     if (file) {
//         const reader = new FileReader();

//         reader.onload = function(e) {
//             const imageContainer = document.getElementById('selected-image-container');
//             const imageElement = document.getElementById('selected-image');
            
//             imageElement.src = e.target.result;
//             imageElement.style.display = 'block'; // Show the image
//             console.log(e.target.result);
//             // Optional: Add the selected image to your post data or perform other actions
//             console.log('Selected Image:', file);
//         };

//         reader.readAsDataURL(file);
//     }
// });

document.querySelector(".Posts").addEventListener("click", async function (event){
    event.preventDefault();
    
    const content = document.querySelector('#postContent').value;
    // const photo = event.target.dataset.image;
    
    await postPost(user, {content});
});