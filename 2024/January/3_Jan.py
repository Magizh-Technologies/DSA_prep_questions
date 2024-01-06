# Set Matrix Zeroes
# Amazon Microsoft
# https://leetcode.com/problems/set-matrix-zeroes/submissions/

# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

# You must do it in place.

# Example 1:

# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]

# Solution:
class Solution:
    def setZeroes(self, matrix):
        rows, cols = len(matrix), len(matrix[0])
        zero_rows, zero_cols = set(), set()

        # Mark the rows and columns that contain zeros
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    zero_rows.add(i)
                    zero_cols.add(j)

        # Set entire rows to zero
        for row in zero_rows:
            for j in range(cols):
                matrix[row][j] = 0

        # Set entire columns to zero
        for col in zero_cols:
            for i in range(rows):
                matrix[i][col] = 0

# Rotate Image
# Microsoft Paytm Samsung Adobe
# https://leetcode.com/problems/rotate-image/

# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

# Example 1:

# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]

# Solution:
class Solution:
    def rotate(self, matrix):
        n = len(matrix)

        # Transpose the matrix
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Reverse each row to complete the rotation
        for i in range(n):
            matrix[i].reverse()
