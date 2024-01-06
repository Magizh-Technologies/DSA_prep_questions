# # Product of Array Except Self
# # Microsoft + Facebook Interview Qs
# # https://leetcode.com/problems/product-of-array-except-self/

# # Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# # The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# # You must write an algorithm that runs in O(n) time and without using the division operation.

# # Example 1:

# # Input: nums = [1,2,3,4]
# # Output: [24,12,8,6]

# # Solution:
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # Initialize two arrays to store products to the left and right of each element
        left_products, right_products = [1] * n, [1] * n

        # Calculate products to the left of each element
        left_product = 1
        for i in range(1, n):
            left_product *= nums[i - 1]
            left_products[i] = left_product

        # Calculate products to the right of each element
        right_product = 1
        for i in range(n - 2, -1, -1):
            right_product *= nums[i + 1]
            right_products[i] = right_product

        # Multiply left and right products for the final result
        result = [left_products[i] * right_products[i] for i in range(n)]

        return result

# Maximum Product Subarray
# Amazon D-E-Shaw Microsoft Morgan Stanley OYO Rooms Google
# https://leetcode.com/problems/maximum-product-subarray/submissions/

# Given an integer array nums, find a 
# subarray that has the largest product, and return the product.

# Example 1:

# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
# Example 2:

# Input: nums = [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

# Solution:
from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0

        current_max = current_min = max_product = nums[0]

        for num in nums[1:]:
            if num < 0:
                current_max, current_min = current_min, current_max

            current_max = max(num, current_max * num)
            current_min = min(num, current_min * num)

            max_product = max(max_product, current_max)

        return max_product

