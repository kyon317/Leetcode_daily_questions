"""
Leetcode 2577. Minimum Time to Visit a Cell In a Grid
https://leetcode.com/problems/minimum-time-to-visit-a-cell-in-a-grid/description/
Finish date: 2024-11-28
Algorithm: Graph, Dijkstra
"""
from heapq import heappop, heappush
from typing import List


class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1
        dis = [[float('inf')] * n for _ in range(m)]
        dis[0][0] = 0
        h = [(0, 0, 0)]  # dis, x, y
        while True:
            d, x, y = heappop(h)
            if d > dis[x][y]:
                continue
            if x == m - 1 and y == n - 1:
                return d
            for nx, ny in (x, y - 1), (x - 1, y), (x, y + 1), (x + 1, y):
                if 0 <= nx < m and 0 <= ny < n:
                    newd = max(d + 1, grid[nx][ny])
                    newd += (newd - nx - ny) % 2
                    if newd < dis[nx][ny]:
                        dis[nx][ny] = newd
                        heappush(h, (newd, nx, ny))
