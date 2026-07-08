class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        l, r = 0, 2
        length = len(s) - 1
        count = 0
        while length >= r:
            sub = s[ l : r+1 ]
            if len(set(sub)) == 3:
                count += 1
            l += 1
            r += 1
        return count
        