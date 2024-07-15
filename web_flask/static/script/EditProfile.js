const urlParams = new URLSearchParams(window.location.search);
const fromPage = urlParams.get('from');

console.log(fromPage);
if (fromPage !== 'profile') {
    let nav =  document.querySelector('.nav');
    let textNav = nav.getElementsByTagName('h2')[0];
    let backImg = nav.getElementsByTagName('a')[0];

    textNav.innerText = "Enter your information";
    nav.removeChild(backImg);
}

document.getElementsByClassName('input')[0].addEventListener('submit', async function (event) {
    event.preventDefault();
    first_name = event.target.first_name
    last_name = event.target.last_name
    bio = event.target.bio
    country = event.target.country
    city = event.target.city
    website = event.target.website

   user = {first_name, last_name, bio, country, city, website}
});