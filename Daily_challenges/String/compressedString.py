"""
Leetcode 3163. String Compression III
https://leetcode.com/problems/string-compression-iii/description/
Finish date: 2024-11-03
Algorithm: String
"""
class Solution:
    def compressedString(self, word: str) -> str:
        comp = []
        cnt,prev = 1,word[0]
        for x in word[1:]:
            if prev == x:
                if cnt == 9:
                    comp.append(str(cnt))
                    comp.append(prev)
                    cnt = 1
                else:
                    cnt += 1
            else:
                comp.append(str(cnt))
                comp.append(prev)
                prev = x
                cnt = 1
        comp.append(str(cnt))
        comp.append(prev)
        return "".join(comp)