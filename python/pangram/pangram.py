from string import ascii_lowercase

def is_pangram(sentence):
    # a-z character list
    compared = list(ascii_lowercase)
    # only alphabet list in sentence
    res = [n for n in (sentence.lower()).replace(' ', '') if n.isalpha()]

    return set(compared) == set(res)    # set type vouch for 'no Overlap'