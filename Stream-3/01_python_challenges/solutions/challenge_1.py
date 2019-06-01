# Function

def count_upper_case(message):
    count = 0
    for c in message:
        if c.isupper():
            count += 1
    return count

assert count_upper_case("") == 0, "Empty string."
assert count_upper_case("A") == 1, "One upper case."
assert count_upper_case("a") == 0, "One lower case."
assert count_upper_case("£$%%^") == 0, "Special characters."


## Modified function

def count_upper_case_upd(message):
    return sum([1 for c in message if c.isupper()]) 


## Additional asserts

try: 
    assert count_upper_case_upd("beOwuLF") == 2, "Should be three upper case letters." # FAIL
except AssertionError:
    print ("Looks like this test failed!")
assert count_upper_case_upd("beOwuLF") == 3, "Three upper case letters." # PASS
assert count_upper_case_upd("JUPITER") == 7, "Seven upper case letters." # PASS
assert count_upper_case_upd("SATUrn") == 4, "Four upper case letters." # PASS
assert count_upper_case_upd("MERcuRY") == 5, "Five upper case letters." # PASS


print("All the tests passed")