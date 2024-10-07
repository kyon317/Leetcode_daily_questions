"""
Leetcode 2696. Minimum String Length After Removing Substrings
https://leetcode.com/problems/minimum-string-length-after-removing-substrings/description/
Finish date: 2024-10-06
Algorithm: Stack, Simulation
"""


class Solution:
    def minLength(self, s: str) -> int:
        'Stack'
        stk = []
        for x in s:
            if stk and ((stk[-1] == 'A' and x == 'B') or (stk[-1] == 'C' and x == 'D')):
                stk.pop()
            else:
                stk.append(x)
        return len(stk)
    # 'Simulation'
    # def minLength(self, s: str) -> int:
    #     while "AB" in s or "CD" in s:
    #         s = s.replace("AB","")
    #         s = s.replace("CD","")
    #     return len(s)
