"""
Leetcode 2501. Longest Square Streak in an Array
https://leetcode.com/problems/longest-square-streak-in-an-array/description/
Finish date: 2024-10-27
Algorithm: DP, Hash
"""

from math import isqrt
from typing import List


class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        dp = {}
        res = -1
        nums.sort()
        for x in nums:
            root = isqrt(x)
            if root*root == x and root in dp:
                dp[x] = 1 + dp[root]
            else:
                dp[x] = 1
            res = max(res, dp[x])
        return res if res > 1 else -1