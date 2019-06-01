$(document).ready(function() {

    // Challenge - The Importance of 'this'

    /* This approach looks at each button in the nav separately. First creating a var streams to get
    the stream number which is then stored in streamNum. This is added to cards to create the variable with
    both the card and stream number (varStreamCard) and the color is then changed to red.
    */
    $('.stream1_btn').on("click", function() {
        var streams = $(this).attr('class').split('_');
        var streamNum = streams[0];
        var cards = ".card-";
        var varStreamCard = cards + streamNum;
        alert("The stream card is " + varStreamCard);
        $(varStreamCard).css("background-color", "#FF0000");
    });

    $('.stream2_btn').on("click", function() {
        var streams = $(this).attr('class').split('_');
        var streamNum = streams[0];
        var cards = ".card-";
        var varStreamCard = cards + streamNum;
        alert("The stream card is " + varStreamCard);
        $(varStreamCard).css("background-color", "#FF0000");
    });

    $('.stream3_btn').on("click", function() {
        var streams = $(this).attr('class').split('_');
        var streamNum = streams[0];
        var cards = ".card-";
        var varStreamCard = cards + streamNum;
        alert("The stream card is " + varStreamCard);
        $(varStreamCard).css("background-color", "#FF0000");
    });


}); // document()
