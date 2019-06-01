# Function counts the number of even elements in a sequence, and if that count is even return True,
# otherwise False

def even_number_of_evens(n):
    if len(n) == 0:
        return False
    result = n[:]
    for element in result:
        if element % 2 != 0:
            result.remove(element)
    if len(result) % 2 == 0:
        return True
        
    return False


## Here are some tests that might suffice for testing our new function.

assert even_number_of_evens([]) == False, "No numbers."
assert even_number_of_evens([2]) == False, "One even number."
assert even_number_of_evens([2, 4]) == True, "Two even numbers."
assert even_number_of_evens([2, 3]) == False, "Two numbers, only one even."
assert even_number_of_evens([2, 3, 9, 10, 13, 7, 8]) == False, "Multiple numbers, three are even."
assert even_number_of_evens([2, 3, 9, 10, 13, 7, 8, 5, 12]) == True, "Multiple numbers, four are even."
assert even_number_of_evens([1, 3, 9]) == False, "No even numbers."


print("All the tests passed")