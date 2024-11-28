from collections import deque
from typing import List


class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        g = [[float('inf')] * n for _ in range(m)]
        g[0][0] = 0
        q = deque([(0, 0)])
        while q:
            x, y = q.popleft()
            for nx, ny in (x, y + 1), (x + 1, y), (x, y - 1), (x - 1, y):
                if 0 <= nx < m and 0 <= ny < n:
                    dis = grid[nx][ny]
                    if dis + g[x][y] < g[nx][ny]:
                        g[nx][ny] = dis + g[x][y]
                        if dis == 0:
                            q.appendleft((nx, ny))
                        else:
                            q.append((nx, ny))
        return g[-1][-1]
