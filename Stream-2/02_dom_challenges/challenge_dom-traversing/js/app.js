$(document).ready(function() {

    console.log('Hello World!');

    
    // $('.card_para').on("click", function() {
    //     $(this).children('a').css("background-color", "yellow");
    // });

    
    // With classes ...

    // $('.card_para').on("click", function() {
    //     $(this).children('a').addClass("highlight");
    // });

    
    /* For button.html */

    // Challenge 1 - Traversing Sideways

    // Make the next element p toggle using .next()

    $('button').next().slideToggle('slow').slideToggle('slow');

    
    // Challenge 2 - Traversing Sideways

    // $('img').on("click", function() {
    //     $(this).parent().children('p').slideDown('slow');
    // });

    
    // Challenge 3 - Traversing Sideways

    // $('.card').on("click", function() {
    //     $(this).next().prev().css("background-color", "pink");
    // });

    
    // With classes ...

    $('.card').click(function() {
        $(this).toggleClass("highlight-pink");
    });

    
    // Challenge 4 - Traversing Sideways

    // First loop through each card and check if it has the highlight-pink class,
    // if so we continue, otherwise we set the display to none

    $('#select').click(function() {
        var cards = document.getElementsByClassName('card');
        var flag = $(cards).hasClass('highlight-pink');

        for (var i = 0; i < cards.length; i++) {
            if ($(cards[i]).hasClass('highlight-pink')) {
                continue;
            }
            else {
                // $(cards[i]).addClass('highlight-pink');
                $(cards[i]).css("display", "none");
            }
        }
    });

    
    // Same as before, except we reverse display:none by using the show() function

    $('#all').click(function() {
        var cards = document.getElementsByClassName('card');

        for (var i = 0; i < cards.length; i++) {
            $(cards[i]).show();
        }
    });






}); // document()
