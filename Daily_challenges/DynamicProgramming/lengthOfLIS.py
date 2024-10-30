"""
Leetcode 300. Longest Increasing Subsequence
https://leetcode.com/problems/longest-increasing-subsequence/description/
Finish date: 2024-10-29
Algorithm: DP, Binary Search
"""

from bisect import bisect
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        g = []
        for i,x in enumerate(nums):
            idx = bisect.bisect_left(g, x)
            if idx == len(g):
                g.append(x)
            else:
                g[idx] = x
        return len(g)