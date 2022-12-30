let menubars = document.querySelector('#menu-bars')
let mynav = document.querySelector('.navbar')


let searchform = document.querySelector('#search-form')
let myform = document.querySelector('.form-search')


menubars.onclick = () =>{
    menubars.classList.toggle('fa-times')
    mynav.classList.toggle('active')
}

searchform.onclick = () =>{

    myform.classList.toggle('active')
}


































// const navbar = document.querySelector('.header')

// window.onscroll = () =>{
//     if(window.scrollY > 300){
//         navbar.classList.add('active')
//     }
//     else{
//         navbar.classList.remove('active')
//     }
// }