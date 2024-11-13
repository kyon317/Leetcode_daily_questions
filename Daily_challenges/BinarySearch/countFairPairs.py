"""
Leetcode 2563. Count the Number of Fair Pairs
https://leetcode.com/problems/count-the-number-of-fair-pairs/description/
Finish date: 2024-11-12
Algorithm: Binary Search, Three Pointers, MergeSort
"""

from bisect import bisect_left, bisect_right
from typing import List


class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        res = 0
        nums.sort()
        # lower <= nums[i] + nums[j] <= upper
        # lower - nums[j] <= nums[i]
        # upper - nums[j] >= nums[i]
        for i, x in enumerate(nums):
            l = bisect_left(nums, lower - x, 0, i)  # # of nums[i] that are smaller than lower - nums[j]
            r = bisect_right(nums, upper - x, 0, i) # # of nums[i] that are no larger than upper - nums[j]
            res += r - l
        return res
