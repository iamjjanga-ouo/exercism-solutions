def decode(string):
    num = 0
    de_str = ""

    # Check String is empty
    if not string:
        return string
    # Check each Character in string
    for c in string:
        if c.isdigit(): # If character is digit, count number
            num *= 10
            num += int(c)
        else:               # If character is letter, append character * count in de_str
            if num == 0:
                de_str += c
            else:
                de_str += c * num
            num = 0

    return de_str

def encode(string):
    en_str = ""

    # Check String is empty
    if not string:
        return string

    string += "." # Character end of string
    i = 1
    while True:
        if string[i] == ".": # Break Loop if end of string
            break
        if string[i-1] != ',' and string[i] != string[i-1]:
            string = string[:i] + "," + string[i:]
        i += 1

    string = string[:len(string)-1] # delete character end of string

    for i in string.split(","):
        if len(i) == 1:
            en_str += i[0]
        else:
            en_str += str(len(i)) + i[0]

    return en_str


########################
# Community Solution Best
########################
# 느낀점 : 아.. 정규표현식 잘써야겠다.
'''
# -*- coding: utf-8 -*-
from re import sub


def encode(s):
    return sub(r'(.)\1+', lambda x: str(len(x.group(0))) + x.group(1), s)


def decode(s):
    return sub(r'(\d+)(\D)', lambda x: x.group(2) * int(x.group(1)), s)
'''
