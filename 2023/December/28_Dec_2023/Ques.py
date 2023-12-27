# Valid Anagram
# Nagarro Media.net Directi Google Adobe Flipkart
# https://leetcode.com/problems/valid-anagram/

# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
# typically using all the original letters exactly once.

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false

# Solution:
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Check if the lengths of the strings are different
        if len(s) != len(t):
            return False

        # Create dictionaries to store character frequencies for both strings
        freq_s = {}
        freq_t = {}

        # Populate the frequency dictionary for string s
        for char in s:
            freq_s[char] = freq_s.get(char, 0) + 1

        # Populate the frequency dictionary for string t
        for char in t:
            freq_t[char] = freq_t.get(char, 0) + 1

        # Check if the frequency dictionaries are equal
        return freq_s == freq_t


# Candy Question
# Amazon Interview Qs
# https://practice.geeksforgeeks.org/problems/candy/1?utm_source=geeksforgeeks&utm_medium=ml_article_practice_tab&utm_campaign=article_practice_tab

# There are N children standing in a line. Each child is assigned a rating value given in the integer array ratings.
# You are giving candies to these children subjected to the following requirements:

# Each child must have atleast one candy.
# Children with a higher rating than its neighbors get more candies than their neighbors.
# Return the minimum number of candies you need to have to distribute.

# Example 1:

# Input:
# N = 3
# ratings = [1, 0, 2]
# Output: 
# 5
# Explanation: 
# You can allocate to the first, second and third child with 2, 1, 2 candies respectively.

# Solution:
class Solution:
    def minCandy(self, N, ratings):
        # Initialize the candies array with 1 candy for each student
        candies = [1] * N

        # Traverse from left to right
        for i in range(1, N):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        # Traverse from right to left
        for i in range(N - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)

        # Return the total number of candies
        return sum(candies)
