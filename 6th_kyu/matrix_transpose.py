# https://www.codewars.com/kata/52fba2a9adcd10b34300094c/python
# DESCRIPTION:
# Write a function that outputs the transpose of a matrix - a new matrix where the columns and rows of the original are swapped.

# For example, the transpose of:

# | 1 2 3 |
# | 4 5 6 |
# is

# | 1 4 |
# | 2 5 |
# | 3 6 |
# The input to your function will be an array of matrix rows. You can assume that each row has the same length, and that the height and width of the matrix are both positive.

def transpose(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    transposed_matrix = [[None] * rows for _ in range(columns)]
    for row_index in range(rows):
        for column_index in range(columns):
            transposed_matrix[column_index][row_index] = matrix[row_index][column_index]
    return transposed_matrix