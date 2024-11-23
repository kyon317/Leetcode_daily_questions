"""
Leetcode 1861. Rotating the Box
https://leetcode.com/problems/rotating-the-box/description/
Finish date: 2024-11-22
Algorithm: Array, Matrix
"""
from typing import List


class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m,n = len(box),len(box[0])
        res = [['.'] * m for _ in range(n)]
        for i in range(m):
            idx = 0
            while idx < n:
                stones = 0
                while idx < n and box[i][idx] != '*':
                    if box[i][idx] == '#':
                        stones += 1
                    idx += 1
                for j in range(idx - stones, idx):
                    res[j][m - 1 - i] = '#'
                if idx < n:
                    res[idx][m - 1 - i] = '*'
                idx += 1
        return res