def score(word):
    my_dict = dict.fromkeys(['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'], 1)
    my_dict.update(dict.fromkeys(['D', 'G'], 2))
    my_dict.update(dict.fromkeys(['B', 'C', 'M', 'P'], 3))
    my_dict.update(dict.fromkeys(['F', 'H', 'V', 'W', 'Y'], 4))
    my_dict.update(dict.fromkeys(['K'], 5))
    my_dict.update(dict.fromkeys(['J', 'X'], 8))
    my_dict.update(dict.fromkeys(['Q', 'Z'], 10))

    # Can make with List comprehension?
    # initial variable("point") in List comprehension doesn't work...
    point = 0
    for char in word:
        point += my_dict.get(char.upper())
    return point