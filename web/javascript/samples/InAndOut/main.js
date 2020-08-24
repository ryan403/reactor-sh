let thisH1 = document.getElementsByTagName("h1")[0];
let thisP = document.getElementsByTagName("p")[0];
let thisDiv = document.getElementsByTagName("div")[0];

function mouseIn(){
    thisH1.innerHTML="你進來了";
}

function mouseOut(){
    thisH1.innerHTML="你出去了";
    thisP.innerHTML="";
}

function mouseMove(e){
    thisP.innerHTML="你在裡面走來走去。位置 : "+e.clientX+","+e.clientY;
}

thisDiv.addEventListener("mouseover", mouseIn);
thisDiv.addEventListener("mouseout", mouseOut);
thisDiv.addEventListener("mousemove", mouseMove);