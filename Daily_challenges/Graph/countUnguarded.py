"""
Leetcode 2257. Count Unguarded Cells in the Grid
https://leetcode.com/problems/count-unguarded-cells-in-the-grid/
Finish date: 2024-11-20
Algorithm: Graph
"""
from typing import List


class Solution:
    def countUnguarded(
            self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]
    ) -> int:
        g = [[0] * n for _ in range(m)]

        # Mark walls with -1
        for r, c in walls:
            g[r][c] = -1

        # Mark guards with -2
        for r, c in guards:
            g[r][c] = -2

        for r, c in guards:
            # Down
            for x in range(r + 1, m):
                if g[x][c] == -1 or g[x][c] == -2:  # Stop at wall or guard
                    break
                g[x][c] = 1
            # Up
            for x in range(r - 1, -1, -1):
                if g[x][c] == -1 or g[x][c] == -2:
                    break
                g[x][c] = 1
            # Right
            for y in range(c + 1, n):
                if g[r][y] == -1 or g[r][y] == -2:
                    break
                g[r][y] = 1
            # Left
            for y in range(c - 1, -1, -1):
                if g[r][y] == -1 or g[r][y] == -2:
                    break
                g[r][y] = 1

        cnt = 0
        for i in range(m):
            for j in range(n):
                if g[i][j] == 0:
                    cnt += 1

        return cnt
