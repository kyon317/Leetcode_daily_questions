"""
Leetcode 2981. Find Longest Special Substring That Occurs Thrice I
https://leetcode.com/problems/find-longest-special-substring-that-occurs-thrice-i/
Finish date: 2024-12-09
Algorithm: Hash, Heap
"""
from collections import defaultdict
from heapq import heappush, heappop


class Solution:
    def maximumLength(self, s: str) -> int:
        dc = defaultdict(list)  # hashmap: k: char, v: max heap
        cnt = 0
        res = 0
        for i, c in enumerate(s):
            cnt += 1
            if i == len(s) - 1 or c != s[i + 1]:
                heappush(dc[c], -cnt)
                cnt = 0
        for ls in dc.values():
            ls.extend([0, 0])  # empty
            L1 = -heappop(ls)
            L2 = -heappop(ls)
            L3 = -heappop(ls)
            res = max(res, L1 - 2, min(L1 - 1, L2), L3)

        return res if res else -1
