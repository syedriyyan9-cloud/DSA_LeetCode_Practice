class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        set_nums = set(nums)
        for item in range(len(nums) + 1):
            if item not in set_nums:
                return item