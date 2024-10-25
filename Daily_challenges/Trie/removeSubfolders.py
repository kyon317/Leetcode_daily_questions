"""
Leetcode 1233. Remove Sub-Folders from the Filesystem
https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/description/
Finish date: 2024-10-24
Algorithm: Trie
"""

from typing import List

class Trie:
    def __init__(self):
        self.children = {}
        self.idx = -1

    def insert(self, i, s):
        node = self
        curr = s.split('/')
        for x in curr[1:]:
            if x not in node.children:
                node.children[x] = Trie()
            node = node.children[x]
        node.idx = i

    def search(self):
        res = []
        def dfs(node):
            if node.idx != -1:
                res.append(node.idx)
                return
            for child in node.children.values():
                dfs(child)
        dfs(self)
        return res

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        trie = Trie()
        res = []
        for i, x in enumerate(folder):
            trie.insert(i, x)
        ids = trie.search()
        for i in ids:
            res.append(folder[i])
        return res