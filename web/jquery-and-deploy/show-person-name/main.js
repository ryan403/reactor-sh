$("img").hover(
    function(){$("p").text($(this).attr("alt"));},
    function(){$("p").text("");});