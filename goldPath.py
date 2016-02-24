"""
Andrew McCann
CS350
Assignment #3

Given a table composed of N x M
cells, each containing some number of
gold coins.  You start from the upper left hand corner and at each step may
go down or to the right.  At each step you collect all the coins that are in
that location.  Find the maximum number of coins you can collect

"""""

# Input: N+1 by M+1 matrix
# Output: Maximum sum of non-zero values within the matrix in a left-right path only.

def gold(matrix):
    # Assume a row of zeros and a column of zeros have been inserted.
    N = len(matrix)    # Rows
    M = len(matrix[0]) # Columns
    for i in range(1, N):
        for j in range(1, M):
                matrix[i,j] += max(matrix[i,j-1], matrix[i-1,j])

    return matrix[N-1, M-1]

