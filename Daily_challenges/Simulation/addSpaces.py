"""
Leetcode 2109. Adding Spaces to a String
https://leetcode.com/problems/adding-spaces-to-a-string/description/
Finish date: 2024-12-02
Algorithm: Simluation
"""
from typing import List


class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        prev = 0
        res = []
        for x in spaces:
            res.append(s[prev:x] + " ")
            prev = x
        res.append(s[prev:])
        return "".join(res)
