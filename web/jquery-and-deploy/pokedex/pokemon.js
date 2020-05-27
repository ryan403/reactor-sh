let id;

for (let i = 1; i <= 151; i++){
    $("body").append('<img id="' + i + 
    '" src="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/' + 
    i + '.png">');
}

$('img').click(function(){
    id = $(this).attr('id');
    parent.$(parent.document).trigger("imageClick",id);
});