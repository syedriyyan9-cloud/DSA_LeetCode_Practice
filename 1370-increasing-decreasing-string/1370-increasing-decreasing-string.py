class Solution:
    def sortString(self, s: str) -> str:
        s_list = sorted(s)
        dictS = {}
        for item in s_list:
            if item in dictS:
                dictS[item] += 1
            else:
                dictS[item] = 1
        result = ""
        while len(result) < len(s):
            for item in dictS:
                if dictS[item] == 0:
                    continue
                result += item
                dictS[item] -= 1
            for item in reversed(dictS):
                if dictS[item] == 0:
                    continue
                result += item
                dictS[item] -= 1
        return result