from typing import List

'''
Leetcode 1331. Rank Transform of an Array
https://leetcode.com/problems/rank-transform-of-an-array/description/
Finish date: 2024-10-01
Algorithm: Sorting, Hash
'''


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rank = {x: idx + 1 for idx, x in enumerate(sorted(set(arr)))}
        return [rank[x] for x in arr]