let confirmAnswer = confirm("你真的確定你想要取消這個服務嗎?");
if(confirmAnswer){
    document.getElementsByTagName("h1")[0].innerHTML = 
    "服務已取消";
}else{
    document.getElementsByTagName("h1")[0].innerHTML = 
    "繼續使用本服務";
}
