"""
Leetcode 2940. Find Building Where Alice and Bob Can Meet
https://leetcode.com/problems/find-building-where-alice-and-bob-can-meet/description/
Finish date: 2024-12-21
Algorithm: Monotonic stack
"""
from bisect import bisect_left
from typing import List


class Solution:
    def leftmostBuildingQueries(
        self, heights: List[int], queries: List[List[int]]
    ) -> List[int]:
        res = [-1] * len(queries)
        qs = [[] for _ in heights]
        for i, (a, b) in enumerate(queries):
            if a > b:
                a, b = b, a
            if a == b or heights[a] < heights[b]:
                res[i] = b
            else:
                qs[b].append((heights[a], i))
        stk = []
        for i in range(len(heights) - 1, -1, -1):
            for x, idx in qs[i]:
                t = bisect_left(stk, -x, key=lambda i: -heights[i]) - 1
                if t >= 0:
                    res[idx] = stk[t]
            while stk and heights[stk[-1]] <= heights[i]:
                stk.pop()
            stk.append(i)
        return res
