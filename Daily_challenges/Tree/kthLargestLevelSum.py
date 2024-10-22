"""
Leetcode 2583. Kth Largest Sum in a Binary Tree
https://leetcode.com/problems/kth-largest-sum-in-a-binary-tree/
Finish date: 2024-10-21
Algorithm: Binary Tree, DFS, BFS
"""



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        res = []

        def dfs(root, level):
            if not root:
                return
            if len(res) <= level:
                res.append(0)
            res[level] += root.val
            dfs(root.left, level + 1)
            dfs(root.right, level + 1)

        dfs(root, 0)
        res.sort(reverse=True)

        return res[k - 1] if len(res) >= k else -1
