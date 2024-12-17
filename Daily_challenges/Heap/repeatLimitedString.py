"""
Leetcode 2182. Construct String With Repeat Limit
https://leetcode.com/problems/construct-string-with-repeat-limit/description/
Finish date: 2024-12-16
Algorithm: Heap, Greedy
"""

from collections import Counter
from heapq import heappush, heappop


class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        res = []
        cnt = Counter(s)
        heap = []
        for c in sorted(cnt, reverse=True):
            heappush(heap, (-ord(c), c, cnt[c]))
        while heap:
            od, c, ct = heappop(heap)
            toAdd = min(ct, repeatLimit)
            res.extend([c] * toAdd)
            ct -= toAdd
            if ct > 0:
                if not heap:
                    break
                od2, c2, ct2 = heappop(heap)
                res.append(c2)
                ct2 -= 1
                if ct2 > 0:
                    heappush(heap, (od2, c2, ct2))
                heappush(heap, (od, c, ct))

        return "".join(res)
