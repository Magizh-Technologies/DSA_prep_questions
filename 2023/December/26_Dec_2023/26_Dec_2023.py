# Maximum Subarray [Medium]
# Microsoft + Facebook Interview Question
# https://leetcode.com/problems/maximum-subarray/

# Given an integer array nums, find the subarray with the largest sum, and return its sum.

# Example 1:
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.

# Example 2:
# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.

# Example 3:
# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

# Solution (Kadane's Algorithm)
# Kadane's Algorithm is a dynamic programming algorithm used to find the maximum subarray sum in an array. 
# The algorithm efficiently handles cases where the array may contain both positive and negative numbers.

class Solution:
    def maxSubArray(self, nums):
        # Check if the array is empty
        if not nums:
            return 0

        # Initialize variables for current sum and maximum sum
        current_sum = max_sum = nums[0]

        # Iterate through the array starting from the second element
        for num in nums[1:]:
            # Update the current sum to either the current element or the sum so far plus the current element
            current_sum = max(num, current_sum + num)

            # Update the maximum sum if the current sum is greater
            max_sum = max(max_sum, current_sum)

        return max_sum


# Next Permutation
# Uber + Goldman Sachs + Adobe Interview Qs
# https://leetcode.com/problems/next-permutation/

# A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

# For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
# The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, 
# if all the permutations of the array are sorted in one container according to their lexicographical order, 
# then the next permutation of that array is the permutation that follows it in the sorted container. 
# If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

# For example, the next permutation of arr = [1,2,3] is [1,3,2].
# Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
# While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
# Given an array of integers nums, find the next permutation of nums.

# The replacement must be in place and use only constant extra memory.
# Example 1:

# Input: nums = [1,2,3]
# Output: [1,3,2]
# Example 2:

# Input: nums = [3,2,1]
# Output: [1,2,3]
# Example 3:

# Input: nums = [1,1,5]
# Output: [1,5,1]

# Solution
class Solution:
    def nextPermutation(self, nums):
        # Find the first element from the right that is smaller than the next element
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        # If such an element is found, find the smallest element to the right of i that is greater than nums[i]
        if i >= 0:
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            # Swap nums[i] and nums[j]
            nums[i], nums[j] = nums[j], nums[i]

        # Reverse the subarray to the right of i
        left, right = i + 1, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1


# Best Time to Buy and Sell Stock
# Amazon, D-E-Shaw Directi, Flipkart, Goldman Sachs Intuit, MakeMyTrip, Microsoft, Ola Cabs, Oracle, Paytm, Pubmatic Quikr, Salesforce, Sapient, Swiggy, Walmart, Media.net, Google
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
# Example 2:

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.

# Solution:
class Solution:
    def maxProfit(self, prices):
        # Check if the list of prices is empty
        if not prices or len(prices) == 1:
            return 0

        # Initialize variables for minimum price and maximum profit
        min_price = prices[0]
        max_profit = 0

        # Iterate through the prices
        for price in prices[1:]:
            # Update the minimum price if the current price is lower
            min_price = min(min_price, price)

            # Update the maximum profit if selling at the current price yields a higher profit
            max_profit = max(max_profit, price - min_price)

        return max_profit
