def is_pangram(sentence):
    # a-z character list
    compared = [chr(n) for n in range(97, 123)]
    # only alphabet list in sentence
    res = [n for n in (sentence.lower()).replace(' ', '') if n.isalpha()]

    return set(compared) == set(res)    # set type vouch for 'no Overlap'