def is_isogram(string):
    hypen = string.count('-') - 1 if '-' in string else 0
    space = string.count(' ') - 1 if ' ' in string else 0
    return len(string.lower()) == (len(set(string.lower())) + hypen + space)
