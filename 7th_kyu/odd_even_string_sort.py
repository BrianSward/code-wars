# https://www.codewars.com/kata/580755730b5a77650500010c/python
# Given a string s. You have to return another string such that even-indexed and odd-indexed characters of s are grouped and groups are space-separated (see sample below)

# Note: 
# 0 is considered to be an even index. 
# All input strings are valid with no spaces
# input: 'CodeWars'
# output 'CdWr oeas'

def sort_my_string(s):
    even_str = ""
    odd_str = ""
    for i, _s in enumerate(s):
        if i % 2 == 0:
            even_str += _s
        else:
            odd_str += _s
    return f'{even_str} {odd_str}'

