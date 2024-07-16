    import { postUser } from "./CRUD_user.js";
    const urlParams = new URLSearchParams(window.location.search);
    const fromPage = urlParams.get('from');

    const user = JSON.parse(localStorage.getItem('user'));
    // console.log(user);

    if (fromPage !== 'profile') {
        let nav =  document.querySelector('.nav');
        let textNav = nav.getElementsByTagName('h2')[0];
        let backImg = nav.getElementsByTagName('a')[0];

        textNav.innerText = "Enter your information";
        nav.removeChild(backImg);   
    }
    else {
        document.querySelector('input[name="first_name"]').value = user.first_name;
        document.querySelector('input[name="last_name"]').value = user.last_name ;
        document.querySelector('input[name="bio"]').value = user.bio ;
        document.querySelector('input[name="country"]').value = user.country ;
        document.querySelector('input[name="city"]').value = user.city ;
        document.querySelector('input[name="website"]').value = user.website ;

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
            ...user,
            first_name,
            last_name,
            bio,
            country,
            city,
            website
        };

        // console.log(userInfo);
        localStorage.setItem('user', JSON.stringify(userInfo));
        if (fromPage !== 'profile') {
            await postUser(userInfo);
        }

    });

