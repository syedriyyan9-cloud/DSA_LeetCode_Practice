class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        length = len(s)
        for index in range(1, length):
            if length % index == 0:
                if s[:index] * (length // index) == s:
                    return True
        return False