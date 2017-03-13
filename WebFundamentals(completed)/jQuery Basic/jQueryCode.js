$(document).ready(function(){

$('#start').click(function(){
	alert("Yay you passed");
});

$('#Hide').click(function(){
	$('#dino1').hide();
})

$('#Show').click(function(){
	$('#dino1').show();
})

$('#Toggle').click(function(){
	$('#dino2').toggle();
})

$('#slideDown').click(function(){
	$('#dino3').slideDown("slow");
})

$('#slideUp').click(function(){
	$('#dino3').slideUp("slow");
})

$('#slideToggle').click(function(){
	$('#dino4').slideToggle("slow");
})

$('#fadeOut').click(function(){
	$('#dino5').fadeOut();
})
$('#fadeIn').click(function(){
	$('#dino5').fadeIn();
})

$('#addClass').click(function(){
	$('#info5').addClass("red");
 })

$('#before').click(function(){
	$('#info6').before("<h1>I told you!!</h1>")
})
$('#after').click(function(){
	$('#info7').after("<h1>Do you believe me yet?</h1>")
})
$('#append').click(function(){
	$('#info8').append("<p>Viola!</p>")
})
$('#html').click(function(){
	$('#info9').html("<p>ASDJFLBJSDHF</p>")
})
$('#attr').click(function(){
	$('#info10').attr("id", "hello")
})
$('#val').click(function(){
	var text = $(this).text();
	$('input').val("     Well Hello There!")
})
$('#text').click(function(){
	$('#info12').text("Surprise!")
})
$('#data').click(function(){
	$( "#info13" ).data( "test", { first: "Well here I am!" } );
		$( "span" ).text( $( "#info13" ).data( "test" ).first );
})



$(document).ready(function(){

var thecounter=0; 
$(document).click(function(){
for(var i=0; i<=151; i++){
thecounter++;
$('body').append('<img class="pokemon" src="http://pokeapi.co/media/img/' +thecounter+ '.png">');
}
});
})






})