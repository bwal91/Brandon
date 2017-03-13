var thecounter=0; 
var count=0;
$(document).ready(function(){



for(var i=0; i<=151; i++){
thecounter++;
count++;
$('body').append('<img class="pokemon" id="' +count+ '" src="http://pokeapi.co/media/img/' +thecounter+ '.png">');
}

})