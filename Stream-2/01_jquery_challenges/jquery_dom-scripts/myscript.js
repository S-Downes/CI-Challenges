$(document).ready(function() {
    $('h1').css('text-decoration', 'underline'); // Underline
    $('li').css('border', '1px solid #CCC'); // Border

    // Using classes defined in style element
    $('h1').addClass('underline');
    $('h1').addClass('border');

    // Challenge - Table colors

    $('th').addClass('thColor');
    $('tr').addClass('cellColor');
    $('tr:even').addClass('cellColorLight');

    // Challenge 2 - Other Traversing Methods

    // When a table header is clicked - highlight the corresponding row

    $('th').click(function() {
        $(this).parent('tr').addClass("selection");
    });

    // When another table header is clicked - highlight this and return others to white

    $('th').click(function() {
        $(this).addClass("white");
    });


});
