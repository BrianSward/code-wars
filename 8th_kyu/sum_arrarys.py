# Write a function that takes an array of numbers and returns the sum of the numbers. The numbers can be negative or non-integer. If the array does not contain any numbers then you should return 0.

def sum_array(a):
    __len = len(a)
    if __len == 0:
        return 0
    sum = 0
    for thing in a:
        sum += thing
    return sum