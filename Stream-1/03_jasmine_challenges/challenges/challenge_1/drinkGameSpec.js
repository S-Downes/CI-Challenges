describe("whatCanIDrink", function() {

    describe("Age switch conditions", function() {

        it("should return the appropriate code block for the if statement where the age condition is met.", function() {
            expect(whatCanIDrink(-1)).toBe(console.log("Sorry. I can’t tell what drink because that age is incorrect!"));
        });

        it("should return the block appropriate for case where age is less than 14.", function() {
            expect(whatCanIDrink(5)).toBe(console.log("Drink Toddy"));
        });

        it("should return the block appropriate for case where age is less than 18.", function() {
            expect(whatCanIDrink(17)).toBe(console.log("Drink Coke"));
        });

        it("should return the block appropriate for case where age is less than 21.", function() {
            expect(whatCanIDrink(18)).toBe(console.log("Drink Beer"));
        });

        it("should return the block appropriate for case where age is less than 130.", function() {
            expect(whatCanIDrink(65)).toBe(console.log("Drink Whiskey"));
        });

        it("should return the else block if no conditions are met.", function() {
            expect(whatCanIDrink(1000)).toBe(console.log("Sorry. I can’t tell what drink because that age is incorrect!"));
        });

    });

});
