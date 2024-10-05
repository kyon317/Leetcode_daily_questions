"""
Leetcode 567. Permutation in String
https://leetcode.com/problems/permutation-in-string/description/
Finish date: 2024-10-04
Algorithm: Sliding window, Hashtable
"""

from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window = {}
        need = Counter(s1)

        tt, l, r = 0, 0, 0
        while r < len(s2):
            c = s2[r]
            r += 1
            # update window
            if c in need:
                window[c] = window.get(c, 0) + 1
                if window[c] == need[c]:
                    tt += 1
            # update left
            while r - l >= len(s1):
                # found matching string
                if tt == len(need):
                    return True
                d = s2[l]
                l += 1
                if d in need:
                    if window[d] == need[d]:
                        tt -= 1
                    window[d] -= 1
        return False
