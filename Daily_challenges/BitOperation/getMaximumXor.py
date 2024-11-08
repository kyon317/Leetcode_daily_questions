"""
Leetcode 1829. Maximum XOR for Each Query
https://leetcode.com/problems/maximum-xor-for-each-query/description/
Finish date: 2024-11-08
Algorithm: Bit Operation
"""

from typing import List


class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        n = len(nums)
        xors = [0] * n
        curr = nums[0]
        xors[n-1] = curr
        for i in range(1, n):
            curr ^= nums[i]
            xors[n - i - 1] = curr
        mx = 2 ** maximumBit - 1
        for i,x in enumerate(xors):
            xors[i] = x ^ mx
        return xors