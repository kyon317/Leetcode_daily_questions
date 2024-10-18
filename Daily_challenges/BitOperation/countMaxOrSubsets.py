"""
Leetcode 2044. Count Number of Maximum Bitwise-OR Subsets
https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/
Finish date: 2024-10-17
Algorithm: Bit operation, DFS
"""

from typing import List


class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        mx, res = 0, 0
        n = len(nums)
        sz = 1 << n  # 2^n
        for x in nums:
            mx = mx | x
        memo = [0] * sz

        for i in range(n):
            j, k = 0, 1 << i
            while j < k:
                temp = memo[j] | nums[i] # add nums[i] to subset
                memo[k | j] = temp # update
                if temp == mx:
                    res += 1
                j += 1
        return res

    # "DFS"
    # def countMaxOrSubsets(self, nums: List[int]) -> int:
    #     mx, res = 0, 0
    #     n = len(nums)
    #     for x in nums:
    #         mx = mx | x

    #     def dfs(i, curr):
    #         nonlocal res
    #         if i == n:
    #             if curr == mx:
    #                 res += 1
    #             return

    #         dfs(i + 1, curr)
    #         dfs(i + 1, curr | nums[i])

    #     dfs(0,0)
    #     return res
