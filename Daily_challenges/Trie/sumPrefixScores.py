'''
Leetcode #2416. Sum of Prefix Scores of Strings
https://leetcode.com/problems/sum-of-prefix-scores-of-strings/
Finish date: 2024-09-24
Algorithm: Trie
'''

class Trie:
    def __init__(self):
        self.children = [None] * 26
        self.count = 0

    def insert(self, word):
        node = self
        for ch in word:
            idx = ord(ch) - ord('a')
            if not node.children[idx]:
                node.children[idx] = Trie()
            node = node.children[idx]
            node.count += 1

    # modified search function
    def search(self, word):
        node = self
        res = 0
        for ch in word:
            idx = ord(ch) - ord('a')
            node = node.children[idx]
            res += node.count
        return res

class Solution:
    def sumPrefixScores(self, words):
        trie = Trie()
        for word in words:
            trie.insert(word)
        res = []

        for word in words:
            res.append(trie.search(word))
        return res