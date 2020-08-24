let thisH1 = document.getElementsByTagName("h1")[0];
thisH1.addEventListener("click",showAlert);

function showAlert(){
    alert("字串長度 : "+thisH1.innerHTML.length+"\n"+
          "World在第"+thisH1.innerHTML.indexOf("World")+"位置"+"\n"+
          "第一個字"+thisH1.innerHTML.split(" ")[0]+"\n"+
          "第二個字"+thisH1.innerHTML.split(" ")[1]);
}
