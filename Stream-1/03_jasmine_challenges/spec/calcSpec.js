describe("Calculator", function() {
    beforeEach(function() {
        calc = new Calculator();
    });

    describe("Add Function", function() {
        it("should take two numbers as parameters and return the sum of those numbers.", function() {
            calc.add(3);
            calc.add(3);
            expect(calc.value).toBe(6);
        });

        it("should not return 8 if the sum of the parameters are not equal to 8.", function() {
            calc.add(20);
            calc.add(7);
            expect(calc.value).toBe(27);
        });

        it("should return an alert if either number is not of type number of undefined.", function() {
            spyOn(window, "alert");
            calc.add("Hello");
            calc.add("World!");
            expect(window.alert).toHaveBeenCalledWith("Please enter two numbers as parameters.")
        });
    });
});
