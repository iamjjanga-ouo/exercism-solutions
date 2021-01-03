from collections import Counter

YACHT = lambda d: 50 if len(set(d)) == 1 else 0
ONES = lambda d: d.count(1) * 1
TWOS = lambda d: d.count(2) * 2
THREES = lambda d: d.count(3) * 3
FOURS = lambda d: d.count(4) * 4
FIVES = lambda d: d.count(5) * 5
SIXES = lambda d: d.count(6) * 6
FULL_HOUSE = lambda d: sum(d) if sorted(Counter(d).values()) == [2,3] else 0
FOUR_OF_A_KIND = lambda d: sum(x * 4 for x in set(d) if d.count(x) > 3)
LITTLE_STRAIGHT = lambda d: 30 if sum(d) == 15 and len(set(d)) == 5 else 0
BIG_STRAIGHT = lambda d: 30 if sum(d) == 20 and len(set(d)) == 5 else 0
CHOICE = lambda d: sum(d)


def score(dice, category):
    if any(not 0 < x < 7 for x in dice):
        raise ValueError("Invalid dice {}".format(dice))

    return category(dice)