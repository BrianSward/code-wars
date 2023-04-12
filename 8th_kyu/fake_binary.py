# https://www.codewars.com/kata/57eae65a4321032ce000002d
# DESCRIPTION:
# Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the resulting string.

# Note: input will never be an empty string

def fake_bin(x):
    print(x)
    return_me = ""
    for char in x:
        if int(char) > 4:
            return_me += "1"
        if int(char) <= 4: 
            return_me += "0"
    return return_me