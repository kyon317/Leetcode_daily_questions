"""
Leetcode 2415. Reverse Odd Levels of Binary Tree
https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/description/
Finish date: 2024-12-19
Algorithm: DFS
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(l, r, lv):
            if not l:
                return
            if lv % 2 == 1:
                l.val, r.val = r.val, l.val
            dfs(l.left, r.right, lv + 1)
            dfs(r.left, l.right, lv + 1)

        if root:
            dfs(root.left, root.right, 1)
        return root
