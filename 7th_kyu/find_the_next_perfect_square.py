# 
# DESCRIPTION:
# You might know some pretty large perfect squares. But what about the NEXT one?

# Complete the findNextSquare method that finds the next integral perfect square after the one passed as a parameter. Recall that an integral perfect square is an integer n such that sqrt(n) is also an integer.

# If the parameter is itself not a perfect square then -1 should be returned. You may assume the parameter is non-negative.

# Examples:(Input --> Output)

# 121 --> 144
# 625 --> 676
# 114 --> -1 since 114 is not a perfect square

def find_next_square(sq):
    x = sq**(1/2)
    x_s = str(x)
    if x_s[-1] == "0":
        x = sq**(1/2)
        y = (x + 1) * (x + 1)
        return y
    return -1