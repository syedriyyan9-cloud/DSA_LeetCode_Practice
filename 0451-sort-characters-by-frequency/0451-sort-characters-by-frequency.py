class Solution:
    def frequencySort(self, s: str) -> str:
        dictS = {}
        for item in s:
            if item in dictS:
                dictS[item] = dictS[item] + 1
            else:
                dictS[item] = 1
        chars = [k for k in dictS.keys()]
        nums = [v for v in dictS.values()]
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    nums[j], nums[i] = nums[i], nums[j]
                    chars[j], chars[i] = chars[i], chars[j]
        new_list = [char * num for char, num in zip(chars, nums)]
        s1 = ""
        s1 = s1.join(new_list)
        return s1