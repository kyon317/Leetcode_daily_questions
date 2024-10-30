"""
Leetcode 1671. Minimum Number of Removals to Make Mountain Array
https://leetcode.com/problems/minimum-number-of-removals-to-make-mountain-array/description/
Finish date: 2024-10-29
Algorithm: DP, Binary Search
"""

from bisect import bisect_left
from typing import List


class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        suf = [0] * n
        g = [] # suffix
        for i in range(n - 1, -1, -1):
            x = nums[i]
            idx = bisect_left(g, x)
            if idx == len(g):
                g.append(x)
            else:
                g[idx] = x
            suf[i] = idx + 1
        f = [] # prefix
        res = 0 # res = max(pre[i] + suf[i] - 1)
        for i,x in enumerate(nums):
            x = nums[i]
            idx = bisect_left(f, x)
            if idx == len(f):
                f.append(x)
            else:
                f[idx] = x
            pre = idx + 1
            if pre > 1 and suf[i] > 1: # need at least one element on both sides
                res = max(res, pre + suf[i] - 1)
        return n - res
