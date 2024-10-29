"""
Leetcode 2684. Maximum Number of Moves in a Grid
https://leetcode.com/problems/maximum-number-of-moves-in-a-grid/description/
Finish date: 2024-10-28
Algorithm: DFS, DP
"""

from typing import List


class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        n,m = len(grid), len(grid[0])
        res = 0
        def dfs(i,j):
            nonlocal res
            res = max(res,j)
            if j == m - 1:
                return
            for k in i-1,i,i+1:
                if 0 <= k < n and grid[k][j+1] > grid[i][j]:
                    dfs(k,j+1)
            grid[i][j] = 0 # Mark as visited, faster than @cache
        for i in range(n):
            dfs(i,0)
        return res