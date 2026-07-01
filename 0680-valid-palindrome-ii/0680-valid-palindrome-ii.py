class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        flag = True
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                # check by removing r char
                s1 = s[:]
                s1 = s1[:r] + s1[r + 1:]
                x, y = 0,len(s1) - 1
                while x < y:
                    if s1[x] == s1[y]:
                        flag = True
                    if s1[x] != s1[y]:
                        flag = False
                        break
                    x += 1
                    y -= 1
                else:
                    break
                # if not flag:
                #     break
                # check by removing l
                s1 = s[:]
                s1 = s1[:l] + s1[l + 1:]
                x, y = 0,len(s1) - 1
                while x < y:
                    if s1[x] == s1[y]:
                        flag = True
                    else:
                        flag = False
                        break
                    x += 1
                    y -= 1
                else:
                    break
                if not flag:
                    break
        if flag:
            return True
        else:
            return False