class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        l = 0
        r = 1
        while l < len(nums) and r < len(nums):
            if l % 2 == 0 and nums[l] % 2 == 0:
                    l += 2
            elif r % 2 == 0 and nums[r] % 2 == 0:
                    r += 2
            elif l % 2 != 0 and nums[l] % 2 != 0:
                    l += 2
            elif r % 2 != 0 and nums[r] % 2 != 0:
                    r += 2
            else:
                nums[r], nums[l] = nums[l], nums[r]
                r += 2
                l += 2
        return nums