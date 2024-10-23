"""
Leetcode 2641. Cousins in Binary Tree II
https://leetcode.com/problems/cousins-in-binary-tree-ii/
Finish date: 2024-10-23
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
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        res = []
        def dfs(root,level):
            if not root:
                return
            if level >= len(res):
                res.append(root.val)
            else:
                res[level] += root.val
            dfs(root.left,level+1)
            dfs(root.right,level+1)

        def update(root,level):
            if not root:
                return
            curr = res[level+1]
            if root.left:
                curr -= root.left.val
            if root.right:
                curr -= root.right.val
            if root.left:
                root.left.val = curr
            if root.right:
                root.right.val = curr
            update(root.left,level+1)
            update(root.right,level+1)
        dfs(root,0)
        res.append(0) # sentinel
        update(root,0)
        root.val = 0
        return root