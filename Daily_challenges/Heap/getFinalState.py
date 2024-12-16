"""
Leetcode 3264. Final Array State After K Multiplication Operations I
https://leetcode.com/problems/final-array-state-after-k-multiplication-operations-i/description/
Finish date: 2024-12-15
Algorithm: Heap
"""
from typing import List


class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for i in range(k):
            mn = min(nums)
            idx = nums.index(mn)
            nums[idx] *= multiplier
        return nums