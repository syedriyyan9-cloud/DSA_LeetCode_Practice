class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        if len(s) < 3:
            return 0
        left = 0
        right = 2
        number = 0
        while right < len(s):
            sets = set()
            count = left
            while count <= right:
                if s[count] not in sets:
                    sets.add(s[count])
                if len(sets) == 3:
                    number += 1
                count += 1
            left += 1
            right += 1
        return number