class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dictST = {}
        dictTS = {}
        for index in range(len(s)):
            char1 = s[index]
            char2 = t[index]
            if ((char1 in dictST and dictST[char1] != char2) or (char2 in dictTS and dictTS[char2] != char1)):
                return False
            dictST[char1] = char2
            dictTS[char2] = char1
        return True