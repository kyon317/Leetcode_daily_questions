"""
Leetcode 3097. Shortest Subarray With OR at Least K II
https://leetcode.com/problems/shortest-subarray-with-or-at-least-k-ii/description/
Finish date: 2024-11-10
Algorithm: Bit operation
"""
from math import inf
from typing import List


class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        dc = dict() # k: v - max OR value: left point
        res = inf
        for i,x in enumerate(nums):
            dc = {OR | x : left for OR, left in dc.items()}
            dc[x] = i # single elem
            for OR, left in dc.items():
                if OR >= k:
                    res = min(res,i-left + 1)
        return res if res < inf else -1