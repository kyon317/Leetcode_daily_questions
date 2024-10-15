"""
Leetcode 2938. Separate Black and White Balls
https://leetcode.com/problems/separate-black-and-white-balls/description/
Finish date: 2024-10-15
Algorithm: String
"""

class Solution:
    def minimumSteps(self, s: str) -> int:
        res = 0
        cnt = 0
        for x in s[::-1]:
            if x == '0':
                cnt += 1
            if x == '1':
                res += cnt
        return res