# Contains Duplicate
# Amazon Interview Qs
# https://leetcode.com/problems/contains-duplicate/

# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Example 1:

# Input: nums = [1,2,3,1]
# Output: true
# Example 2:

# Input: nums = [1,2,3,4]
# Output: false
# Example 3:

# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true

# Solution:
class Solution:
    def containsDuplicate(self, nums):
        # Create a set to store unique elements
        unique_elements = set()

        # Iterate through the array
        for num in nums:
            # If the element is already in the set, it's a duplicate
            if num in unique_elements:
                return True
            # Otherwise, add the element to the set
            unique_elements.add(num)

        # If the loop completes without finding duplicates, return False
        return False

# Search in Rotated Sorted Array
# Microsoft Google Adobe Amazon D-E-Shaw Flipkart Hike Intuit MakeMyTrip Paytm 
# https://leetcode.com/problems/search-in-rotated-sorted-array/

# There is an integer array nums sorted in ascending order (with distinct values).

# Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:

# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1

# Solution:
class Solution:
    def search(self, nums, target):
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:
                # Left half is sorted
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                # Right half is sorted
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1


# Repeat and Missing Number Array
# Amazon Interview Qs
# https://www.interviewbit.com/problems/repeat-and-missing-number-array/

# There are certain problems which are asked in the interview to also check how you take care of overflows in your problem.

# This is one of those problems.

# Please take extra care to make sure that you are type-casting your ints to long properly and at all places. Try to verify if your solution works if number of elements is as large as 105

# Food for thought :

# Even though it might not be required in this problem, in some cases, you might be required to order the operations cleverly so that the numbers do not overflow.
# For example, if you need to calculate n! / k! where n! is factorial(n), one approach is to calculate factorial(n), factorial(k) and then divide them.
# Another approach is to only multiple numbers from k + 1 ... n to calculate the result.
# Obviously approach 1 is more susceptible to overflows.
# You are given a read only array of n integers from 1 to n.

# Each integer appears exactly once except A which appears twice and B which is missing.

# Return A and B.

# Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

# Note that in your output A should precede B.

# Example:

# Input:[3 1 2 5 3] 

# Output:[3, 4] 

# A = 3, B = 4

# Solution:
class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        n = len(A)
        # Calculate the sum of numbers and sum of squares
        sum_n = n * (n + 1) // 2
        sum_sq = n * (n + 1) * (2 * n + 1) // 6

        # Calculate the actual sum and sum of squares
        actual_sum = sum(A)
        actual_sum_sq = sum(x*x for x in A)

        # Calculate the difference
        diff_sum = actual_sum - sum_n
        diff_sum_sq = actual_sum_sq - sum_sq

        # Calculate the missing and repeating numbers
        missing_number = (diff_sum + diff_sum_sq // diff_sum) // 2
        repeating_number = missing_number - diff_sum

        return [missing_number ,repeating_number]