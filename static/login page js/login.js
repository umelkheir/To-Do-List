const name = document.getElementById("name");
const form = document.getElementById("form");



// adding an eventlistener that guides the user to the to do list.
form.addEventListener('submit', (e) =>{
    e.preventDefault();


    const userName = name.value;
    localStorage.setItem('name', userName);
    window.location.href = "/index"




})
