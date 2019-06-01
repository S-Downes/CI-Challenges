# Function(s)

def test_are_equal(actual, expected):
    assert expected == actual, "Expected {0}, got {1}".format(expected, actual)


def test_not_equal(a, b):
    assert a != b, "Did not expect {0}, but got {1}".format(a, b)


def test_is_in(collection, item):
    assert item in collection, "{0} does not contain {1}".format(collection, item)  


def test_between(val, lower_lim, upper_lim):
    assert val > lower_lim and val < upper_lim, "{0} is between the range {1} and {2}".format(val, lower_lim, upper_lim)
    
    
## Here are some tests that might suffice for testing our new function.

test_set = ["Hello", 1, 5, 13, "", "Moon", "Sun", "Star"]

test_are_equal(True, True) # PASS
test_not_equal(2, 2) # FAIL
test_not_equal(7, 7) # FAIL
test_is_in(test_set, "World") # FAIL
test_is_in(test_set, [2, 3]) # FAIL
test_between(2, 3, 100) # FAIL
test_between(54, 3, 100) # PASS


print("All the tests passed")