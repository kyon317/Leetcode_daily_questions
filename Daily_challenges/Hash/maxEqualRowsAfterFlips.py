"""
Leetcode 1072. Flip Columns For Maximum Number of Equal Rows
https://leetcode.com/problems/flip-columns-for-maximum-number-of-equal-rows/description/
Finish date: 2024-11-21
Algorithm: Hashmap, Matrix, Graph
"""
from collections import Counter
from typing import List


class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        cnt = Counter()
        for r in matrix:
            if r[0]:
                for j in range(len(r)):
                    r[j] ^= 1
            cnt[tuple(r)] += 1
        return max(cnt.values())