"""
Leetcode 1014. Best Sightseeing Pair
https://leetcode.com/problems/best-sightseeing-pair/description/
Finish date: 2024-12-26
Algorithm: DP
"""
from typing import List


class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        res = mx = 0
        for i, x in enumerate(values):
            res = max(res, mx + x - i)
            mx = max(mx, x + i)
        return res