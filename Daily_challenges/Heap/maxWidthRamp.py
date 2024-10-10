"""
Leetcode 962. Maximum Width Ramp
https://leetcode.com/problems/maximum-width-ramp/description/
Finish date: 2024-10-09
Algorithm: Monotonic Stack
"""

from typing import List


class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stk = []
        for i, x in enumerate(nums):
            if not stk or nums[i] < nums[stk[-1]]:
                stk.append(i)
        res, n = 0, len(nums)
        for j in range(n - 1, -1, -1):
            while stk and nums[j] >= nums[stk[-1]]:
                curr_len = j - stk.pop()
                if curr_len > res:
                    res = curr_len
        return res
