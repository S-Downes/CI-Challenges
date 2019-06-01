$(document).ready(function() {

	/* Sample Code
	$("#stream1_btn").on("click", function() {
		$(".stream1").removeClass('highlight_stream');
		$(".stream2").removeClass('highlight_stream');
		$(".stream3").removeClass('highlight_stream');
		$(".stream1").addClass('highlight_stream');
	});
	$("#stream2_btn").on("click", function() {
		$(".stream1").removeClass('highlight_stream');
		$(".stream2").removeClass('highlight_stream');
		$(".stream3").removeClass('highlight_stream');
		$(".stream2").addClass('highlight_stream');
	});
	$("#stream3_btn").on("click", function() {
		$(".stream1").removeClass('highlight_stream');
		$(".stream2").removeClass('highlight_stream');
		$(".stream3").removeClass('highlight_stream');
		$(".stream3").addClass('highlight_stream');
	});
	*/
	
	// Challenge - Card Panel

	$('p').click(function() {
		$('p').addClass('bg-red');
	});

	$('h2').hover(function() {
		$('h2').addClass('bg-lightBlue');
	});

	// Adjust the font-size for the h2 element in the event only

	$('h2').hover(function() {
		$(this).addClass('lg-fontSize');
	});

	// Using .hover() to first change the bg to black on hover and leaving, bg to grey

	$('[href]').hover(function() {
		$('body').addClass('bg-black');
	}, function() {
		$('body').addClass('bg-grey');
	});

	//  Or using mouseenter - mouseleave

	$('[href]').mouseenter(function() {
		$('body').addClass('bg-black');
	});

	$('[href]').mouseleave(function() {
		$('body').addClass('bg-grey');
	});


	// Challenge - jQuery Effects

	$('button:first').click(function() {
		$(this).hide("slow");
		$(this).hide("medium");
		$(this).hide("fast");
		$(this).hide(2000);

	});
	

	// Challenge 2- jQuery Effects

	$('.bottom_button').click(function() {
		$('.card_para:first').Toggle("medium");
	});
	
	
	// Challenge 3 - jQuery Effects

	$('.bottom_button').click(function() {
		$('.card_para:first').slideToggle("medium");
	});
	
	
	// Challenge 4 - jQuery Effects

	$('.bottom_button:first').mouseenter(function() {
		$(this).fadeTo("slow", 0.5);
	});
	
	$('.bottom_button:first').mouseleave(function() {
		$(this).fadeTo("slow", 1.0);
	});
	
	
	





});//.ready()
