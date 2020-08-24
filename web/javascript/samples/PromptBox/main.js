let promptAnswer = 
    prompt("小明家裡有三個小孩，他兩個哥哥叫張一、張二、第三個小孩叫什麼?",
           "張三");

switch(promptAnswer){
    case "張三":
        document.getElementById("Response").innerHTML = 
        "那小明是誰?";
        break;
    case "小明":
        document.getElementById("Response").innerHTML = 
        "聰明";
        break;
    default:
        document.getElementById("Response").innerHTML = 
        "你想多了";
}
