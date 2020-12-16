def abbreviate(words):
    # think more pythonic...
    import re
    # convert 'punctuation_without_whitespace' ex. (metal-oxide) to (metal oxide)
    words = re.sub('-',' ', words)
    # convert except of alphabet, number, one space to blank
    words = re.sub(r'[^\ a-zA-Z0-9]','',words)
    # make more than 2 space be a one space for split
    words = re.sub(r'\ {2,}',' ', words)
    return ''.join([letter[0].upper() for letter in words.split(' ')])

    ## community solution I think best
    # pattern = re.compile("[A-Z]+['a-z]*|['a-z]+")
    # return ''.join(word.group()[0].upper() for word in pattern.finditer(words))