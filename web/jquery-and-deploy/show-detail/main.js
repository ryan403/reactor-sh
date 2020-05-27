$("p").hide(); //先隱藏段落
$("button").click(function(){ //當按鈕按下後
    $("p").toggle(500,function(){});	  //切換顯示段落	
});	