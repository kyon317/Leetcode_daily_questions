"""
Leetcode 2924. Find Champion II
https://leetcode.com/problems/find-champion-ii/description/
Finish date: 2024-11-25
Algorithm: Graph
"""
from typing import List


class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        g = [0] * n
        for x,y in edges:
            g[y] += 1
        res = -1
        for i,x in enumerate(g):
            if x == 0:
                if res != -1:
                    return -1
                else:
                    res = i
        return res