"""
Leetcode 2490. Circular Sentence
https://leetcode.com/problems/circular-sentence/description/
Finish date: 2024-11-01
Algorithm: String
"""

class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        st = sentence.split(" ")
        for i,x in enumerate(st[:-1]):
            if x[-1] != st[i+1][0]:
                return False
        return st[-1][-1] == st[0][0]