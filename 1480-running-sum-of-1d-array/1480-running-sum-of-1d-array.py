class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        num1 = 0
        length = len(nums)
        output = []
        for index in range(length):
            num1 += nums[index]
            if index != 0:
                output += [num1]
            else:
                output += [num1]
        return output