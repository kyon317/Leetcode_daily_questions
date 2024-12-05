"""
Leetcode 2337. Move Pieces to Obtain a String
https://leetcode.com/problems/move-pieces-to-obtain-a-string/description/
Finish date: 2024-12-05
Algorithm: Two pointers
"""
class Solution:
    def canChange(self, start: str, target: str) -> bool:
        if start.replace("_","") != target.replace("_",""):
            return False
        idx = 0
        for i, c in enumerate(start):
            if c == '_':
                continue
            while target[idx] == "_":
                idx += 1
            if i != idx:
                if c == "L" and i < idx:
                    return False
                if c == "R" and i > idx:
                    return False
            idx += 1
        return True