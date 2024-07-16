    import { postUser } from "./CRUD_user.js";
    const urlParams = new URLSearchParams(window.location.search);
    const fromPage = urlParams.get('from');

    const storedUser = JSON.parse(localStorage.getItem('user'));
    console.log(storedUser);

    if (fromPage !== 'profile') {
        let nav =  document.querySelector('.nav');
        let textNav = nav.getElementsByTagName('h2')[0];
        let backImg = nav.getElementsByTagName('a')[0];

        textNav.innerText = "Enter your information";
        nav.removeChild(backImg);

        
    }


    document.getElementsByClassName('input')[0].addEventListener('submit', async function (event) {
        event.preventDefault();
        const first_name = event.target.first_name.value;
        const last_name = event.target.last_name.value;
        const bio = event.target.bio.value;
        const country = event.target.country.value;
        const city = event.target.city.value;
        const website = event.target.website.value;

        const userInfo = {
            ...storedUser,
            first_name,
            last_name,
            bio,
            country,
            city,
            website
        };
        console.log(userInfo);
        localStorage.setItem('user', JSON.stringify(userInfo));
        if (fromPage !== 'profile') {
            await postUser(userInfo);
        }

    });

