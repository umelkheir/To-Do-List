// const list = document.getElementsByClassName('.no-li');




// list.classList.contains('.no-li');

function toggle(){
    if(list.classList.contains('no-li')){
        list.classList.remove("no-li");
    } else{
        list.classList.add('no-li');
    }
}



const list = document.getElementsByTagName('li');
const className = document.getElementsByClassName('toggle');


for(i=0; i<list.length; i++){

    const el = list[i];
    el.addEventListener('click', () => {
    el.classList.toggle('toggle');
    });
    className.addEventListener('click', toggle);
}


// // const button = document.getElementById("button"); 
// const classNamePressed = (e) => {
//   e.target.classList.toggle("toggle");
// }
// className.addEventListener("click", classNamePressed);





// function edit(){
//     if(list == "Overdue"){
//         list.style.textDecoration = "line-through";
//         }
    
// }

// function toggle(){

// }

// function editItem(){
//     if (list == "Overdue"){
//         list.style.textDecoration = "line-through";
//     }
// }


// editItem();




