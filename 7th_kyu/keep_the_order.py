# https://www.codewars.com/kata/582aafca2d44a4a4560000e7
# Task:
# Your job here is to write a function (keepOrder in JS/CoffeeScript, keep_order in Ruby/Crystal/Python, keeporder in Julia), which takes a sorted array ary and a value val, and returns the lowest index where you could insert val to maintain the sorted-ness of the array. The input array will always be sorted in ascending order. It may contain duplicates.

# Do not modify the input.

def keep_order(ary, val):
    if len(ary) == 0:
        return 0
    for i, x in enumerate(ary):
        if x >= val:
            if i == len(ary):
                return len(ary)
            return i
    return len(ary)