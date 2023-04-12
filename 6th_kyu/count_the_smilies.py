# DESCRIPTION:
# Given an array (arr) as an argument complete the function countSmileys that should return the total number of smiling faces.

# Rules for a smiling face:

# Each smiley face must contain a valid pair of eyes. Eyes can be marked as : or ;
# A smiley face can have a nose but it does not have to. Valid characters for a nose are - or ~
# Every smiling face must have a smiling mouth that should be marked with either ) or D
# No additional characters are allowed except for those mentioned.

# Valid smiley face examples: :) :D ;-D :~)
# Invalid smiley faces: ;( :> :} :]

def count_smileys(arr):
    counter = 0
    for thing in arr:
        if len(thing) == 2:
            if thing[0] == ":" or thing[0] == ";":
                if thing[-1] == 'D' or thing[-1] == ')':
                    counter += 1
        if len(thing) == 3:
            if thing[0] == ":" or thing[0] == ";":
                if thing[1] == "-" or thing[1] == "~":
                    if thing[-1] == 'D' or thing[-1] == ')':
                        counter += 1
    return counter