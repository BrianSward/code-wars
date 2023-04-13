# https://www.codewars.com/kata/56a5d994ac971f1ac500003e/train/python
# You are given an array(list) strarr of strings and an integer k. Your task is to return the first longest string consisting of k consecutive strings taken in the array.

def longest_consec(strarr, k):
    n = len(strarr)
    if n == 0 or k > n or k <= 0:
        return ""
    pointer = n - k + 1
    poss_ans =  ""
    poss_ans_len = 0
    for i in range(pointer):
        _ = ''.join(strarr[i:i+k])
        _len = len(_)
        if _len > poss_ans_len:
            poss_ans = _
            poss_ans_len = len(poss_ans)
    return poss_ans