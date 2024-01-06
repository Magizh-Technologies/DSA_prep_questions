# Kth Largest Element in an Array
# Amazon Microsoft Walmart Adobe
# https://leetcode.com/problems/kth-largest-element-in-an-array/description/

# Given an integer array nums and an integer k, return the kth largest element in the array.

# Note that it is the kth largest element in the sorted order, not the kth distinct element.

# Can you solve it without sorting?

 

# Example 1:

# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5
# Example 2:

# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4

# Solution:
import heapq

class Solution:
    def findKthLargest(self, nums, k):
        # Convert the list to a min heap
        heap = nums[:k]
        heapq.heapify(heap)

        # Iterate through the rest of the array
        for num in nums[k:]:
            # If the current number is larger than the smallest element in the heap, replace it
            if num > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, num)

        # The kth largest element is the smallest element in the heap
        return heap[0]


# Trapping Rain Water
# Samsung Interview Qs
# https://leetcode.com/problems/trapping-rain-water/description/

# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

# Example 1:


# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

# Solution:
class Solution:
    def trap(self, height):
        n = len(height)
        if n <= 2:
            return 0

        left_max, right_max = [0] * n, [0] * n

        # Calculate the maximum height to the left of each bar
        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], height[i])

        # Calculate the maximum height to the right of each bar
        right_max[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])

        trapped_water = 0

        # Calculate the trapped water at each bar
        for i in range(1, n - 1):
            min_side = min(left_max[i - 1], right_max[i + 1])
            if min_side > height[i]:
                trapped_water += min_side - height[i]

        return trapped_water
