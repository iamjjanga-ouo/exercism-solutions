from collections import Counter

def find_anagrams(word, candidates):
    res = []
    for string in candidates:
        if string.lower() == word.lower():  # When test words are themselves, pass
            continue

        # Count character in word using collections.Counter. (dictionary format)
        elif Counter(string.lower()) == Counter(word.lower()):
            res.append(string)

    return res


    ## Want : Coding to using 'List comprehension' by one line
    ## but, multiple if conditional is difficult
    # return [string for string in candidates if (Counter(string.lower()) == Counter(word.lower()))]
