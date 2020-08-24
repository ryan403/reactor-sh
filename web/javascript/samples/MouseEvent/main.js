$("div").mouseover(function(){
    $("h1").text("你進來了");
});

$("div").mouseout(function(){
    $("h1").text("你出去了");
    $("p").text("");
});

$("div").mousemove(function(){
    $("p").text("你在裡面走來走去");
});
