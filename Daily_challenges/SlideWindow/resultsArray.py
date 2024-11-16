"""
Leetcode 3254. Find the Power of K-Size Subarrays I
https://leetcode.com/problems/find-the-power-of-k-size-subarrays-i/description/
Finish date: 2024-11-16
Algorithm: Sliding Window
"""
from typing import List


class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        res = []
        n = len(nums)
        if k == 1:
            return nums
        l,r = 0,1
        while r < n:
            if nums[r] - nums[r - 1] != 1:
                while l < r and l + k - 1 < n:
                    res.append(-1)
                    l += 1
            elif r - l + 1 == k:
                res.append(nums[r])
                l += 1
            r += 1
        return res