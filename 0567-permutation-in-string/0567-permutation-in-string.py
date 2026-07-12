class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l, r = 0, len(s1)
        flag = True
        # window = [:r]
        while r <= len(s2):
            if s1[0] in s2:
                window = s2[l : r]
                if sorted(s1) == sorted(window):
                    return True
            r += 1
            l += 1
        return False