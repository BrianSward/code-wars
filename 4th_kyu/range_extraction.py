# https://www.codewars.com/kata/51ba717bb08c1cd60f00002f/train/python
# A format for expressing an ordered list of integers is to use a comma separated list of either

# individual integers
# or a range of integers denoted by the starting integer separated from the end integer in the range by a dash, '-'. The range includes all integers in the interval including both endpoints. It is not considered a range unless it spans at least 3 numbers. For example "12,13,15-17"
# Complete the solution so that it takes a list of integers in increasing order and returns a correctly formatted string in the range format.

def solution(args):
    ranges = []
    start = end = None

    for num in args:
        if start is None:
            start = num
            end = num
        elif num == end + 1:
            end = num
        else:
            ranges.append((start, end))
            start = num
            end = num

    if start is not None:
        ranges.append((start, end))

    return ','.join(helper(start, end) for start, end in ranges)


def helper(start, end):
    if start == end:
        return str(start)
    elif end - start >= 2:
        return f'{start}-{end}'
    else:
        return f'{start},{end}'
