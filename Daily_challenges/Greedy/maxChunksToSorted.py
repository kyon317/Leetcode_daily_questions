"""
Leetcode 769. Max Chunks To Make Sorted
https://leetcode.com/problems/max-chunks-to-make-sorted/description/
Finish date: 2024-12-18
Algorithm: Greedy
"""
from typing import List


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        mx = -1
        res = 0
        for i, x in enumerate(arr):
            # A[:K + 1] = [0,1,2...,k]
            mx = max(mx, x)
            if mx == i:
                res += 1
        return res
