var counter = 0
var idcount = 0
$(document).ready(function(){
for(var i=0; i<=151; i++){
thecounter++;
idcount++;
$('body').append('<img class="pokemon" id="'+idcount+'" src="http://pokeapi.co/media/img/' +thecounter+ '.png">');
}
	$.get("http://pokeapi.co/api/v1/pokemon/1/", function(res) {
                    var html_str = "";
                    html_str += "<h4>Types</h4>";
                    html_str += "<ul>"; 
                    for(var i = 0; i < res.types.length; i++) {
                        html_str += "<li>" + res.types[i].name + "</li>";
                    }
                    html_str += "</ul>";
                    $("#bulbasaur").html(html_str);
                }, "json");




})