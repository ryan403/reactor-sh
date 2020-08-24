window.onload = function(){
    document.onclick = function(e){
        alert(e.target.innerHTML + "有" + 
              e.target.innerHTML.length+"個字元");
    };
}; 
