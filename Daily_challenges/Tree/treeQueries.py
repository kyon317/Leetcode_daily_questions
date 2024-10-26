"""
Leetcode 2458. Height of Binary Tree After Subtree Removal Queries
https://leetcode.com/problems/height-of-binary-tree-after-subtree-removal-queries/description/
Finish date: 2024-10-25
Algorithm: DFS
"""


from collections import defaultdict
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        height = defaultdict(int)
        def get_height(node: Optional[TreeNode]) -> int:
            if node is None: return 0
            height[node] = 1 + max(get_height(node.left), get_height(node.right))
            return height[node]
        get_height(root)

        res = [0] * (len(height) + 1)
        def dfs(node: Optional[TreeNode], depth: int, rest_h: int) -> None:
            if node is None: return
            depth += 1
            res[node.val] = rest_h
            dfs(node.left, depth, max(rest_h, depth + height[node.right]))
            dfs(node.right, depth, max(rest_h, depth + height[node.left]))
        dfs(root, -1, 0)

        for i, q in enumerate(queries):
            queries[i] = res[q]
        return queries