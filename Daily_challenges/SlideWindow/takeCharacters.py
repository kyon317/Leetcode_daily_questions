"""
Leetcode 2516. Take K of Each Character From Left and Right
https://leetcode.com/problems/take-k-of-each-character-from-left-and-right/description/
Finish date: 2024-11-19
Algorithm: Sliding Window, Hashmap
"""

from collections import Counter


class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        cnt = Counter(s)
        res = 0
        if cnt['a'] < k or cnt['b'] < k or cnt['c'] < k:
            return -1
        left = 0
        for i,x in enumerate(s):
            cnt[x] -= 1
            while cnt[x] < k:
                cnt[s[left]] += 1
                left += 1
            res = max(res, i - left + 1)
        return len(s) - res