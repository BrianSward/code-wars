# https://www.codewars.com/kata/54ba84be607a92aa900000f1
# DESCRIPTION:
# An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

# Example: (Input --> Output)

# "Dermatoglyphics" --> true "aba" --> false "moOse" --> false (ignore letter case)

def is_isogram(string):
    if len(string) == 0:
        return True
    net = set()
    for x in string:
        if x.lower() in net:
            return False
        else:
            net.add(x.lower())
    return True