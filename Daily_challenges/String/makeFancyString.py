"""
Leetcode 1957. Delete Characters to Make Fancy String
https://leetcode.com/problems/delete-characters-to-make-fancy-string/description/
Finish date: 2024-10-31
Algorithm: String
"""

class Solution:
    def makeFancyString(self, s: str) -> str:
        res = []
        cnt, pre = 0, ""
        for x in s:
            if x == pre:
                cnt += 1
            else:
                cnt = 0
            pre = x
            if cnt < 2:
                res.append(x)
        return "".join(res)
