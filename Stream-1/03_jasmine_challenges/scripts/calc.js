
/* Our Basic addition() function for testing

function addition(nOne, nTwo) {
    if (typeof(nOne) == "number" && typeof(nTwo) == "number") {
        return nOne + nTwo;
    }
    else {
        alert("Please enter two numbers as parameters.");
    }
}

*/

// Now let's change our function completely and update our tests

Calculator = function() {
    this.value = 0;
}

Calculator.prototype.add = function(num) {
    if (typeof(num) == "number") {
        this.value += num;
    }
    else {
        alert("Please enter two numbers as parameters.");
    }
}
