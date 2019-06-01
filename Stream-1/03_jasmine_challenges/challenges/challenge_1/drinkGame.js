function whatCanIDrink(age) {

    if (age < 0) {
        console.log("Sorry. I can’t tell what drink because that age is incorrect!");
    }
    if (age > 0 && age < 14) {
        console.log("Drink Toddy");
    }
    if (age > 14 && age < 18) {
        console.log("Drink Coke");
    }
    if (age > 18 && age < 21) {
        console.log("Drink Beer");
    }
    if (age > 21 && age < 130) {
        console.log("Drink Whiskey");
    }
    else {
        console.log("Sorry. I can’t tell what drink because that age is incorrect!");
    }

}// whatCanIDrink()


function whatCanIDrink(age) {
    
    switch (age) {
        case (age < 0):
            console.log("Sorry. I can’t tell what drink because that age is incorrect!");
            break;
        case (age < 14):
            console.log("Drink Toddy");
            break;
        case (age < 18):
            console.log("Drink Coke");
            break;
        case (age < 21):
            console.log("Drink Beer");
            break;
        case (age < 130):
            console.log("Drink Whiskey");
            break;
        default:
            console.log("Sorry. I can’t tell what drink because that age is incorrect!");
    }

} // whatCanIDrink()
