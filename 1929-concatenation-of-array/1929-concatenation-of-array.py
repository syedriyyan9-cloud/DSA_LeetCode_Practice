class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        length = len(nums)
        length_twice = len(nums) * 2
        count = 0
        ans = []
        for index in range(length_twice):
            if index != 0 and index % length == 0:
                count = 0
            ans += [nums[count]]
            count += 1
        return ans