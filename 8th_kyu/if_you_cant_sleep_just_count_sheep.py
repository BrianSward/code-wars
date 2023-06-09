# https://www.codewars.com/kata/5b077ebdaf15be5c7f000077
# If you can't sleep, just count sheep!!

# Task:
# Given a non-negative integer, 3 for example, return a string with a murmur: "1 sheep...2 sheep...3 sheep...". Input will always be valid, i.e. no negative integers.

def count_sheep(n):
    _counter = 0
    bucket = ""
    while n > 0:
        _counter += 1
        bucket += f'{_counter} sheep...'
        n -= 1
    return bucket