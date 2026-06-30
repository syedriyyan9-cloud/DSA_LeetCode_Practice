class Solution:
    def isPalindrome(self, s: str) -> bool:
        # two pointer approach
        s1 = ""
        for char in s:
            if char.isdigit() or char.isalpha():
                s1 += char.lower()
        l = 0
        r = len(s1) - 1
        while l < r:
            if s1[l] != s1[r]:
                return False
            l += 1
            r -= 1
        return True
            
