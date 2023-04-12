# https://www.codewars.com/kata/5592e3bd57b64d00f3000047
# Your task is to construct a building which will be a pile of n cubes. The cube at the bottom will have a volume of n^3, the cube above will have volume of (n−1)^3 and so on until the top which will have a volume of 1^3.

# You are given the total volume m of the building. Being given m can you find the number n of cubes you will have to build?

def find_nb(m):
    n = 0
    while (n * (n + 1) // 2) ** 2  < m:
        n += 1
    if (n * (n + 1) // 2) ** 2 == m:
        return n
    return -1