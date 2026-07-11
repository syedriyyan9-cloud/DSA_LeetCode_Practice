class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        b_code = set()
        l = 0

        for r in range(k, len(s)+1):
            if s[l:r] not in b_code:
                b_code.add(s[l:r])
            l += 1
                
        if len(b_code) == 2 ** k:
            return True
        else:
            return False