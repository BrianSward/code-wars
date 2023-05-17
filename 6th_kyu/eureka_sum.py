# https://www.codewars.com/kata/5626b561280a42ecc50000d1/python
# The number 89 is the first integer with more than one digit that fulfills the property partially introduced in the title of this kata. What's the use of saying "Eureka"? Because this sum gives the same number: 
# 89 = 8^1 + 9^2 
# The next number in having this property is 135

# Task
# We need a function to collect these numbers, that may receive two integers 
# # a, b that defines the range [a,b] (inclusive) and outputs a list of the sorted numbers in the range that fulfills the property described above.

def sum_dig_pow(a, b):
    eureka_numbers = []
    for num in range(a, b + 1):
        digits = []
        for index, digit in enumerate(str(num)):
            _item = int(digit) ** (index + 1)
            digits.append(_item)
        total = sum(digits)
        if total == num:
            eureka_numbers.append(num)
    return eureka_numbers