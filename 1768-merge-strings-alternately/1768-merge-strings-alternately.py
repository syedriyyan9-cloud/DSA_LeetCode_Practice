class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        p1 = 0
        p2 = 0
        merge = ""
        while p1 < len(word1) or p2 < len(word2):
            if p1 < len(word1):
                merge += word1[p1]
                p1 += 1
            if p2 < len(word2):
                merge += word2[p2]
                p2 += 1
        return merge      