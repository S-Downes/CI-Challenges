$(document).ready(function() {
 //
 // add your jQuery code here
 $('#button1').addClass('makeRed');

 $('#button1').hover(function() {
  $('#button1').mouseenter(function() {
   $(this).removeClass('makeRed').addClass('makeBorder');
  });
  $('#button1').mouseleave(function() {
   $(this).removeClass('makeBorder').addClass('makeRed');
  });

 }); // .hover()

 // Challenge 2 - Method Chaining
 $('#button1, #button2').mouseup(function() {
  $('p').slideUp('medium');

 });

 $('#button1, #button2').mousedown(function() {
  $('p').slideDown('medium');

 });

 // Challenge 3 - Method Chaining
 $('#button1, #button2').click(function() {
  $('p').show('medium').hide();
  $(this).fadeIn('medium').fadeOut('medium').fadeIn('medium');

 });


}); // document()
