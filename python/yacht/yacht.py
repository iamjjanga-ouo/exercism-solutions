"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""


# Score categories.
# Change the values as you see fit.
YACHT = [5]
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = [3, 2]
FOUR_OF_A_KIND = [4]
LITTLE_STRAIGHT = list(range(1, 6))   # [1,2,3,4,5]
BIG_STRAIGHT = list(range(2, 7))      # [2,3,4,5,6]
CHOICE = None

'''
>>> z = [1,2,3,5,5]
>>> Counter(z)
Counter({5: 2, 1: 1, 2: 1, 3: 1})
>>> list(Counter(z).values())
[1, 2, 3, 5]            # When make dict_values to list, Sorting is happened
>>> max(list(Counter(z)).values())
5
'''
from collections import Counter
def score(dice, category):
    dice_dict = Counter(dice)
    combi_list = list(sorted(list(dice_dict.values()), reverse=True)) # Sort dict_value reverse

    # return max(dice_dict.keys(), key=(lambda k: dice_dict[k]))
    # return max(dice_dict, key=dice_dict.get)

    max_combi = combi_list[0]
    second_combi = 0
    if len(combi_list) > 1:
        second_combi = combi_list[1]

    if category == ONES:
        return dice.count(ONES) * ONES
    elif category == TWOS:
        return dice.count(TWOS) * TWOS
    elif category == THREES:
        return dice.count(THREES) * THREES
    elif category == FOURS:
        return dice.count(FOURS) * FOURS
    elif category == FIVES:
        return dice.count(FIVES) * FIVES
    elif category == SIXES:
        return dice.count(SIXES) * SIXES
    # --------
    elif category == YACHT:     # YACHT
        if max_combi == YACHT[0]:
            return 50
        return 0
    elif category == FOUR_OF_A_KIND:    # FOUR_OF_A_KIND
        if max_combi >= FOUR_OF_A_KIND[0]:
            return max(dice_dict, key=dice_dict.get) * FOUR_OF_A_KIND[0]
        return 0
    elif category == FULL_HOUSE:  # FULL_HOUSE
        if [max_combi, second_combi] == FULL_HOUSE:
            return max(dice_dict, key=dice_dict.get) * max_combi + list(dice_dict.keys())[-2] * second_combi
        return 0
    elif category == LITTLE_STRAIGHT:    # LITTLE_STRAIGHT
        if sorted(dice) == LITTLE_STRAIGHT:
            return 30
        return 0
    elif category == BIG_STRAIGHT:       # BIG_STRAIGHT
        if sorted(dice) == BIG_STRAIGHT:
            return 30
        return 0
    else: # CHOICE
        return sum(dice)


if __name__ == '__main__':
    print(BIG_STRAIGHT)