"""
Leetcode 2275. Largest Combination With Bitwise AND Greater Than Zero
https://leetcode.com/problems/largest-combination-with-bitwise-and-greater-than-zero/description/
Finish date: 2024-11-07
Algorithm: Bit Operation
"""

from typing import List


class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        res = 0
        # 10^7 < 2 ^ 24
        for i in range(24):
            temp = 0
            for x in candidates:
                temp += x >> i & 1
            res = max(temp,res)
        return res