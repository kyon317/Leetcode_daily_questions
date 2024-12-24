"""
Leetcode 3203. Find Minimum Diameter After Merging Two Trees
https://leetcode.com/problems/find-minimum-diameter-after-merging-two-trees/
Finish date: 2024-12-23
Algorithm: Graph, Tree
"""
from typing import List


class Solution:
    def getDiameter(self, edges: List[List[int]]):
        res = 0
        g = [[] for _ in range(len(edges) + 1)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)

        def dfs(x, fa):
            nonlocal res
            mx = 0
            for y in g[x]:
                if y != fa:
                    curr = dfs(y, x) + 1
                    res = max(res, mx + curr)
                    mx = max(curr, mx)
            return mx

        dfs(0, -1)
        return res

    def minimumDiameterAfterMerge(
        self, edges1: List[List[int]], edges2: List[List[int]]
    ) -> int:
        d1 = self.getDiameter(edges1)
        d2 = self.getDiameter(edges2)
        return max(d1, d2, (d1 + 1) // 2 + (d2 + 1) // 2 + 1)
