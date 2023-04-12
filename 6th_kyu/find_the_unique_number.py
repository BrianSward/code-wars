# https://www.codewars.com/kata/585d7d5adb20cf33cb000235
# There is an array with some numbers. All numbers are equal except for one. Try to find it!

def find_uniq(arr):
    dic = {}
    for item in arr:
        if not item in dic:
            dic[item] = 1
        else:
            dic[item] += 1
    for thing in dic.items():
        if thing[1] == 1:
            return thing[0]