# https://www.codewars.com/kata/5656b6906de340bd1b0000ac
# DESCRIPTION:
# Take 2 strings s1 and s2 including only letters from a to z. Return a new sorted string, the longest possible, containing distinct letters - each taken only once - coming from s1 or s2.

def longest(a1, a2):
    bucket = set()
    
    for char in a1:
        bucket.add(char)
    
    for _char in a2:
        bucket.add(_char)
    bucket = list(bucket)
    bucket.sort()
    bucket = "".join(bucket)
    return bucket