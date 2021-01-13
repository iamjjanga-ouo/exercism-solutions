from re import sub

def decode(string):
    return sub(r'(\d+)(\D)', lambda x: int(x.group(1)) * x.group(2), string)
# (\d+)(\D)는 1개이상의 숫자 + 문자를 의미
# 만약 12WB12W3B24WB 라면 12W,12W,3B,24W만 매칭되어서 lambda함수를 통해 변형된다.
# 매칭되지 않는 값들은 그대로 있음.

def encode(string):
    return sub(r'(.)\1+', lambda x: str(len(x.group(0))) + x.group(1), string)
# (.)\1+ 같의 글자의 반복을 의미
# group(0)은 매칭된 문자 전체를 return
































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
