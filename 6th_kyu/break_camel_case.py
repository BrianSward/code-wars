# https://www.codewars.com/kata/5208f99aee097e6552000148/python
# DESCRIPTION:
# Complete the solution so that the function will break up camel casing, using a space between words.

# Example
# "camelCasing"  =>  "camel Casing"
# "identifier"   =>  "identifier"
# ""             =>  ""

def solution(s):
    t = ""
    for char in s:
        if char.isupper():
            t += " "
            t += char
        else:
            t += char
    return t

# without using method just make
# def solution(s):
# t = ""
# look_for_me = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
# for char in s:
#     if char in look_for_me:
#         t += " "
#         t += char
#     else:
#         t += char
# return t 