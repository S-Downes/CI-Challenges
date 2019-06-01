describe("fizzBuzz", function() {

    describe("Conditions that are to be returned based on the value given.", function() {

        it("should return Fizz if the number is divisible by 3 with no remainder.", function() {
            expect(fizzBuzz(9)).toBe("Fizz");
        });

        it("should return Buzz if the number is divisible by 5 with no remainder.", function() {
            expect(fizzBuzz(50)).toBe("Buzz");
        });

        it("should return FizzBuzz if the number is both divisible by 3 and 5 with no remainder.", function() {
            expect(fizzBuzz(15)).toBe("FizzBuzz");
        });

        it("should return the number if it is not divisible by 3 or 5.", function() {
            expect(fizzBuzz(1)).toBe(1);
        });

    });

});
