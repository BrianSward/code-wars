# https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1/solutions/python
# Count the number of Duplicates
# Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.

def duplicate_count(text):
    text = text.lower()
    _dict = {}
    for letter in text:
        if letter.isalnum():
            if letter in _dict:
                _dict[letter] += 1
            else:
                _dict[letter] = 1
    count = 0
    for _item in _dict:
        if _dict[_item] > 1:
            count += 1
    return count