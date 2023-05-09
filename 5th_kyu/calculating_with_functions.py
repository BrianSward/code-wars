# https://www.codewars.com/kata/525f3eda17c7cd9f9e000b39/solutions/python
# This time we want to write calculations using functions and get the results. Let's have a look at some examples:

# seven(times(five())) # must return 35
# four(plus(nine())) # must return 13
# eight(minus(three())) # must return 5
# six(divided_by(two())) # must return 3
# Requirements:

# There must be a function for each number from 0 ("zero") to 9 ("nine")
# There must be a function for each of the following mathematical operations: plus, minus, times, divided_by
# Each calculation consist of exactly one operation and two numbers
# The most outer function represents the left operand, the most inner function represents the right operand
# Division should be integer division. For example, this should return 2, not 2.666666...:
# eight(divided_by(three()))

def zero(option=None):
    num = 0
    if not option:
        return num
    else:
        return _helper(option,num)
    
def one(option=None):
    num = 1
    if not option:
        return num
    else:
        return _helper(option,num)
    
def two(option=None):
    num = 2
    if not option:
        return num
    else:
        return _helper(option,num)
    
def three(option=None):
    num = 3
    if not option:
        return num
    else:
        return _helper(option,num)
    
def four(option=None):
    num = 4
    if not option:
        return num
    else:
        return _helper(option,num)
    
def five(option=None): 
    num = 5
    if not option:
        return num
    else:
        return _helper(option,num)
    
def six(option=None):
    num = 6
    if not option:
        return num
    else:
        return _helper(option,num)
    
def seven(option=None): 
    num = 7
    if not option:
        return num
    else:
        return _helper(option,num)
    
def eight(option=None): 
    num = 8
    if not option:
        return num
    else:
        return _helper(option,num)
    
def nine(option=None):
    num = 9
    if not option:
        return num
    else:
        return _helper(option,num)

def plus(num):
    return f'+ {num}'
def minus(num): 
    return f'- {num}'
def times(num):
    return f'* {num}'
def divided_by(num):
    return f'/ {num}'

def _helper(option, _num):
    scratch_pad = int(option[-1])
    if option[0] == "+":
        scratch_pad += _num
    if option[0] == "-":
        scratch_pad = _num - scratch_pad
    if option[0] == "*":
        scratch_pad = scratch_pad * _num
    if option[0] == "/":
        scratch_pad =  _num // scratch_pad
    return scratch_pad
    