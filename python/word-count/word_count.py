def count_words(sentence):
    import re
    filter_list = []
    ## split sentence any whitespace form (space, newline, comma, underscore)
    for word in re.split(r'[^\'\"a-zA-Z0-9]', sentence.lower()):
        if word == '':
            continue
        if re.match('[a-z]+[\'][a-z]+', word):  # skip single apostrophe
            filter_list.append(word)
            continue
        filter_list.append(re.sub(r'[^\w\d]','',word)) # other special character replace to ''

    my_dict = {}
    for word in filter_list:
        my_dict[word] = my_dict.get(word,0) + 1
    return my_dict

# community solutions
'''
import re
from collections import Counter


def count_words(sentence):
    pattern = re.compile(r"[a-z0-9]+(['][a-z0-9]+)?")

    return Counter(word.group() for word in pattern.finditer(sentence.lower()))
'''