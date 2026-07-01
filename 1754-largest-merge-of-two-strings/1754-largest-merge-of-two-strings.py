class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        i = 0
        j = 0
        merge = ""
        while i < len(word1) and j < len(word2):
            if word1[i] > word2[j]:
                merge += word1[i]
                i += 1
            elif word1[i] < word2[j]:
                merge += word2[j]
                j += 1
            else:
                x = i
                y = j
                while (
                    x < len(word1)
                    and y < len(word2)
                    and word1[x] == word2[y]
                ):
                    x += 1
                    y += 1
                if y == len(word2):
                    merge += word1[i]
                    i += 1
                elif x == len(word1):
                    merge += word2[j]
                    j += 1
                elif word1[x] > word2[y]:
                    merge += word1[i]
                    i += 1
                else:
                    merge += word2[j]
                    j += 1
        merge += word1[i:]
        merge += word2[j:]
        return merge