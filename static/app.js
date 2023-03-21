
// Created a Hello() function that welcomes the user to the to do list using the local storage.
function Hello(){
    const title = document.getElementById("title");
    // retrieves the username from the local storage and displays it.
    const name = localStorage.getItem("name");

    title.innerText = "Welcome " + name;

}

Hello();
