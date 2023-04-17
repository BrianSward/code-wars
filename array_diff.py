# https://www.codewars.com/kata/523f5d21c841566fde000009
# Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.

# It should remove all values from list a, which are present in list b keeping their order.

def array_diff(a, b):
    bucket = [x for x in a if x not in b]
    return bucket