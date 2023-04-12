# https://www.codewars.com/kata/5842df8ccbd22792a4000245
# Write Number in Expanded Form
# You will be given a number and you will need to return it as a string in Expanded Form. For example:

# expanded_form(12) # Should return '10 + 2'
# expanded_form(42) # Should return '40 + 2'
# expanded_form(70304) # Should return '70000 + 300 + 4'
# NOTE: All numbers will be whole numbers greater than 0.

def expanded_form(num):
    bucket = ""
    num = str(num)
    counter_balance = len(num)
    for i, x in enumerate(num):
        if x == '0':
            pass
        else:
            if len(bucket) == 0:
                bucket += (x + (counter_balance-i-1)*"0")
            else:
                bucket += " + " + (x + (counter_balance-i-1)*"0")
    return bucket