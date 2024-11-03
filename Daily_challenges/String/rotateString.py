"""
Leetcode 796. Rotate String
https://leetcode.com/problems/rotate-string/description/
Finish date: 2024-11-02
Algorithm: String
"""
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for i,x in enumerate(s):
            if x == goal[0]:
                ss = s[i:] + s[:i]
                if ss == goal:
                    return True
        return False