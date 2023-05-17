# https://www.codewars.com/kata/52597aa56021e91c93000cb0/python
# Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

# move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]

def move_zeros(lst):
    dummy = lst[:]  # make a copy of the list
    counter = 0
    for i, thing in enumerate(lst):
        if thing == 0:
            dummy.pop(i - counter)
            counter += 1
    while counter > 0:
        dummy.append(0)
        counter -= 1
    return dummy