document.addEventListener('DOMContentLoaded', () => {
    const loggedInUser = JSON.parse(localStorage.getItem('loggedInUser'));

    if (!loggedInUser) {
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
    const firstName = loggedInUser.name.split(' ')[0].toLowerCase();
    
    // Update innerText or attributes with user data
    nameElement.innerText = loggedInUser.name;
    usernameElement.innerText = "@it's_" + firstName;
    bioElement.innerText = loggedInUser.bio || `Hi! I am ${firstName}👋️`;
    linkElement.href = 'https://www.linkedin.com';
    contactElement.href = "mailto:" + loggedInUser.email;
    locationElement.innerHTML = "Al Isma'iliyah, Egypt   " + locationElement.innerHTML;
});