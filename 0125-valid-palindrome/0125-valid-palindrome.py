class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s1 = ""
        for element in s:
            if element.isalpha() or element.isdigit():
                s1 += element
        s2 = s1[:]
        s1 = ""
        for element in s2[::-1]:
            s1 += element
        if s1 == s2:
            return True
        else:
            return False
