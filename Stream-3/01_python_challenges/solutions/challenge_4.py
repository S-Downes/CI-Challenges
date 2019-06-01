# Function

from byo_test import *

usd_coins = [100, 50, 25, 10, 5, 1]
eur_coins = [100, 50, 20, 10, 5, 2, 1]

usd_coins_dict = {100: 20, 50: 20, 25: 20, 10: 20, 5: 20, 1: 20}
eur_coins_dict = {100: 20, 50: 20, 20: 20, 10: 20, 5: 20, 2: 20, 1: 20}

def get_change(amount, coins=eur_coins):
    
    change = []
    for coin in coins:
        while coin <= amount:
            amount -= coin
            change.append(coin)
            
    return change


# Modified to be used with dictionary of coins and amounts

"""
def get_change_dictionary(amount, coins=eur_coins_dict):

    if amount == 0:
        change = {}
    
    for coin, amount in coins.items():
            while coin <= amount:
                amount -= coin
                change[coin] = amount
    
    return change
"""


test_are_equal(get_change_dictionary(0),{})
test_are_equal(get_change_dictionary(1),{1})
test_are_equal(get_change_dictionary(2),{2})
test_are_equal(get_change_dictionary(5),{5})
test_are_equal(get_change_dictionary(10),{10})
test_are_equal(get_change_dictionary(20),{20})
test_are_equal(get_change_dictionary(50),{50})
test_are_equal(get_change_dictionary(100),{100})
test_are_equal(get_change_dictionary(3),{2,1})
test_are_equal(get_change_dictionary(7),{5,2})
test_are_equal(get_change_dictionary(9),{5,2,2})
test_are_equal(get_change_dictionary(35, usd_coins_dict),{25,10})


print("All tests pass!")