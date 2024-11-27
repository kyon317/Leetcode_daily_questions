"""
Leetcode 3243. Shortest Distance After Road Addition Queries I
https://leetcode.com/problems/shortest-distance-after-road-addition-queries-i/description/
Finish date: 2024-11-26
Algorithm: BFS, Graph
"""
from collections import deque
from typing import List


class Solution:
    def shortestDistanceAfterQueries(
            self, n: int, queries: List[List[int]]
    ) -> List[int]:
        g = [[i + 1] for i in range(n - 1)]

        def bfs(i):
            vis = [-1] * n
            q = deque([0])
            vis[0] = 0
            while q:
                curr = q.popleft()
                for y in g[curr]:
                    if vis[y] == -1:
                        vis[y] = vis[curr] + 1
                        q.append(y)
                    if y == n - 1:
                        return vis[y]
            return -1

        res = [0] * len(queries)
        for i, (x, y) in enumerate(queries):
            g[x].append(y)
            res[i] = bfs(i)
        return res
