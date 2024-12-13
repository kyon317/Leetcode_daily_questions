"""
Leetcode 2593. Find Score of an Array After Marking All Elements
https://leetcode.com/problems/find-score-of-an-array-after-marking-all-elements/
Finish date: 2024-12-12
Algorithm: Simulation, Hash
"""
from typing import List


class Solution:
    def findScore(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        vis = [False] * (n + 2)
        for i,x in sorted(enumerate(nums, 1), key = lambda p:p[1]):
          if not vis[i]:
            res += x
            vis[i-1] = vis[i+1] = True
        return res