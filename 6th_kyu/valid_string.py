# https://www.codewars.com/kata/52f3bb2095d6bfeac2002196/python
# DESCRIPTION:
# You are given a sequence of valid words and a string. Test if the string is made up by one or more words from the array.

# Task
# Test if the string can be entirely formed by consecutively concatenating words of the dictionary.

# For example:

# dictionary: ["code", "wars"]

# s1:         "codewars" =>  true  -> match 'code', 'wars'
# s2:         "codewar"  =>  false -> match 'code', unmatched 'war'
# One word from the dictionary can be used several times.

def valid_word(seq, word): 
    n = len(word)
    word_set = set(seq)
    dp = [False] * (n + 1)
    dp[n] = True  
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n + 1):
            if word[i:j] in word_set and dp[j]:
                dp[i] = True
                break

    return dp[0]