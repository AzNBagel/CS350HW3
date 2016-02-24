


""""
Andrew McCann
CS350
Assignment #3

Given a table composed of N x M
cells, each containing some number of
gold coins.  You start from the upper left hand corner and at each step may
go down or to the right.  At each step you collect all the coins that are in
that location.  Find the maximum number of coins you can collect

"""""

# Input: N by M matrix
# Output: Maximum sum of non-zero values within the matrix in a left-right path only.

def gold(matrix):
    maxGold = []

    # Assume a row of zeros and a column of zeros have been inserted.
    for i in range(1, width(matrix+1)):
        for j in range(1, len(matrix)):
                matrix[i,j] += max(matrix[i,j-1], matrix[i-1,j])

    return maxGold[N, M]
