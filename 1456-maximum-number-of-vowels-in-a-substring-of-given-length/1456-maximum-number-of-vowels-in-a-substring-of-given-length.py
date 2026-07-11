class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a','e','i','o','u'}
        l = 0
        maxx = 0
        cur = 0
        for r in range(len(s)):
            if s[r] in vowels:
                cur += 1
            if r - l + 1> k:
                if s[l] in vowels:
                    cur -= 1
                l += 1
            maxx = max(maxx, cur)
        return maxx