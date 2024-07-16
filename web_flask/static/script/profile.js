document.addEventListener('DOMContentLoaded', () => {
    const user = JSON.parse(localStorage.getItem('user'));
    console.log(user);
    if (!user) {
        // Redirect to login page if no user is logged in
        window.location.href = 'login.html';
        return;
    }

    // Select elements and store them in variables
    const nameElement = document.querySelector(".Name");
    const usernameElement = document.querySelector(".Username");
    const bioElement = document.querySelector(".Bio");
    const linkElement = document.querySelector(".Link");
    const locationElement = document.querySelector(".Location");
    const contactElement = document.querySelector(".Contact");
    const followersElement = document.querySelector(".Followers");
    
    // Update innerText or attributes with user data
    nameElement.innerText = user.first_name + ' ' +user.last_name;
    usernameElement.innerText = "@" + user.username || `@it's_${user.first_name.toLowerCase()}`;
    bioElement.innerText = user.bio || `Hi! I am ${user.first_name.toLowerCase()}👋️`;
    linkElement.href = user.website ||'https://www.linkedin.com';
    contactElement.href = "mailto:" + user.email;
    locationElement.innerHTML = user.country +', '+ user.city + ' '+ locationElement.innerHTML;
});