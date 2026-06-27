class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merge = ""
        shorter_string = word1 if len(word1) < len(word2) else word2
        longer_string = word1 if len(word1) > len(word2) else word2
        for index in range(len(shorter_string)):
            merge += word1[index]
            merge += word2[index]
        for index in range(len(shorter_string), len(longer_string)):
            merge += longer_string[index]
        return merge
        