class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indicies = {}
        length = len(nums)
        for index, item in enumerate(nums):
            indicies[item] = index
        for index in range(length):
            s_index = target - nums[index]
            if s_index in indicies:
                if indicies.get(s_index) != index:
                    return [index, indicies.get(target - nums[index])]          
            