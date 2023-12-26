# Maximum size rectangle binary sub-matrix with all 1s
# Amazon Microsoft
# https://practice.geeksforgeeks.org/problems/max-rectangle/1?utm_source=geeksforgeeks&utm_medium=article_practice_tab&utm_campaign=article_practice_tab

# Given a binary matrix, find the maximum size rectangle binary-sub-matrix with all 1’s. 

# Example: 

# Input:
# 0 1 1 0
# 1 1 1 1
# 1 1 1 1
# 1 1 0 0

# Output :
# 8

# Explanation : 
# The largest rectangle with only 1's is from 
# (1, 0) to (2, 3) which is
# 1 1 1 1
# 1 1 1 1 
# and area is 4 *2 = 8.

# Solution
class Solution:
    def maxArea(self, matrix, row, col):
        # Convert the matrix to a histogram representation
        heights = [0] * col
        max_area = 0

        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 1:
                    heights[j] += 1
                else:
                    heights[j] = 0

            # Calculate the maximum area rectangle under the current histogram
            max_area = max(max_area, self.largestRectangleArea(heights))

        return max_area

    def largestRectangleArea(self, heights):
        stack = []
        max_area = 0
        i = 0

        while i < len(heights):
            if not stack or heights[i] >= heights[stack[-1]]:
                stack.append(i)
                i += 1
            else:
                top = stack.pop()
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, heights[top] * width)

        while stack:
            top = stack.pop()
            width = i if not stack else len(heights) - stack[-1] - 1
            max_area = max(max_area, heights[top] * width)

        return max_area


# Word Search
# Google + Ola + Goldman Sachs IQ
# https://leetcode.com/problems/word-search/

# Given an m x n grid of characters board and a string word, return true if word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. 
# The same letter cell may not be used more than once.

# Example 1:
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# Output: true

# Example 2:
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
# Output: true

# Example 3:
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
# Output: false

# Solution:
class Solution:
    def exist(self, board, word):
        if not board or not board[0]:
            return False

        rows, cols = len(board), len(board[0])

        def backtrack(row, col, word_index):
            # Base case: If we reach the end of the word, it means we found a valid path
            if word_index == len(word):
                return True

            # Check if the current cell is within bounds and matches the current letter of the word
            if 0 <= row < rows and 0 <= col < cols and board[row][col] == word[word_index]:
                # Mark the current cell as visited by temporarily changing its value
                original_value = board[row][col]
                board[row][col] = '#'

                # Explore adjacent cells in all four directions
                if (
                    backtrack(row + 1, col, word_index + 1) or
                    backtrack(row - 1, col, word_index + 1) or
                    backtrack(row, col + 1, word_index + 1) or
                    backtrack(row, col - 1, word_index + 1)
                ):
                    return True

                # Backtrack by restoring the original value of the current cell
                board[row][col] = original_value

            return False

        # Iterate through each cell as a starting point for the word search
        for i in range(rows):
            for j in range(cols):
                if backtrack(i, j, 0):
                    return True

        return False


# Valid Palindrome
# Amazon Cisco D-E-Shaw Facebook FactSet Morgan Stanley Paytm Zoho
# https://leetcode.com/problems/valid-palindrome/

# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.

# Solution:
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Filter out non-alphanumeric characters and convert to lowercase
        s = ''.join(char.lower() for char in s if char.isalnum())
        
        # Check if the filtered string is equal to its reverse
        return s == s[::-1]

