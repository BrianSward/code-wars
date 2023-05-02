# https://www.codewars.com/kata/55c45be3b2079eccff00010f/solutions/python
# DESCRIPTION:
# Your task is to sort a given string. Each word in the string will contain a single number. This number is the position the word should have in the result.

# Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

# If the input string is empty, return an empty string. The words in the input String will only contain valid consecutive numbers.

# Examples
# "is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
# "4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"
# ""  -->  ""

def order(sentence):

    words = sentence.split()
    sorted_words = [None] * len(words)

    
    for word in words:
        digits = ""
        for char in word:
            if char.isdigit():
                digits += char
        if digits == "":
            return ""
        position = int(digits)
        sorted_words[position - 1] = word
        
    return " ".join(sorted_words)