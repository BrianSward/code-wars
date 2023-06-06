# https://www.codewars.com/kata/5467e4d82edf8bbf40000155/solutions/python
# Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.

# Examples:
# Input: 42145 Output: 54421

# Input: 145263 Output: 654321

# Input: 123456789 Output: 987654321

def descending_order(num):
    num = str(num)
    bucket = []
    for _digit in num:
        bucket.append(_digit)
    bucket.sort(reverse=True)
    num = "".join(bucket)
    return int(num)