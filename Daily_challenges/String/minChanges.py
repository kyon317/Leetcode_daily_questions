"""
Leetcode 2914. Minimum Number of Changes to Make Binary String Beautiful
https://leetcode.com/problems/minimum-number-of-changes-to-make-binary-string-beautiful/
Finish date: 2024-11-04
Algorithm: String
"""
class Solution:
    def minChanges(self, s: str) -> int:
        n = len(s)
        res = 0
        for i in range(0,n,2):
            if s[i] != s[i+1]:
                res += 1
        return res