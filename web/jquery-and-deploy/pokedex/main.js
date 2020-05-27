$(document).on("imageClick",function(e,id){
    $.get("https://pokeapi.co/api/v2/pokemon/" + id + "/", function(res) {
        //顯示名子
        let nameString = "<h1>" + id+"<br>"+ res.name + "</h1>";
        $('.name').html(nameString);
        //顯示圖片
        let imgString = '<img src="';
        imgString += res.sprites["front_default"] +'">';
        $('.picture').html(imgString);
        //巡訪並顯示類別
        var types = "<h3>Types</h3><ul>";
        for(let i = 0; i < res.types.length; i++) {
            types += "<li>" + res.types[i]["type"].name + "</li>";
        }
        types += "</ul>";
        $(".types").html(types);
        //顯示高度、重量
        $('.height').html("<h3>Height</h3>"+res.height);
        $('.weight').html("<h3>Weight</h3>"+res.weight);
    }, 'json');
});