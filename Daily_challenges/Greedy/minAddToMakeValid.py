"""
Leetcode 921. Minimum Add to Make Parentheses Valid
https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/description/
Finish date: 2024-10-08
Algorithm: Stack, Greedy
"""

class Solution:
    'Greedy'
    def minAddToMakeValid(self, s: str) -> int:
        cnt = 0
        res = 0
        for x in s:
            if x == '(':
                cnt += 1
            if x == ')':
                cnt -= 1
            if cnt < 0:
                cnt = 0
                res += 1
        return res + cnt
    # 'Stack'
    # def minAddToMakeValid(self, s: str) -> int:
    #     stk = []
    #     res = 0
    #     for x in s:
    #         if x == '(':
    #             stk.append(x)
    #         if x == ')':
    #             if stk and stk[-1] == '(':
    #                 stk.pop()
    #             else:
    #                 res += 1
    #     return len(stk) + res