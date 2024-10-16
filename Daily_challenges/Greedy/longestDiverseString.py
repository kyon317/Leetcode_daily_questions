"""
Leetcode 1405. Longest Happy String
https://leetcode.com/problems/longest-happy-string/description/
Finish date: 2024-10-15
Algorithm: Greedy
"""

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = []
        cnt = [[a, 'a'], [b, 'b'], [c, 'c']]
        while True:
            cnt.sort(key=lambda x: -x[0])
            hasNext = False
            for i, (count, d) in enumerate(cnt):
                if count <= 0:
                    break
                if len(res) >= 2 and res[-2] == d and res[-1] == d:
                    continue
                hasNext = True
                res.append(d)
                cnt[i][0] -= 1
                break
            if not hasNext:
                return ''.join(res)