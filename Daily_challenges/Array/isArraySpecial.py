"""
Leetcode 3152. Special Array II
https://leetcode.com/problems/special-array-ii/description/
Finish date: 2024-12-08
Algorithm: Prefix Sum
"""
from typing import List


class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(nums)
        prefix_sum = [0] * n
        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i - 1] + int(nums[i - 1] % 2 == nums[i] % 2)
        res = []
        for l, r in queries:
            curr = prefix_sum[r] == prefix_sum[l]
            res.append(curr)
        return res
