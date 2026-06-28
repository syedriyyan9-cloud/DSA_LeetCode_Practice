class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dict_nums = {}
        for num in nums:
            if num in dict_nums:
                dict_nums[num] = dict_nums[num] + 1
            else:
                dict_nums[num] = 1
        num_tuple = tuple((k,v) for k, v in dict_nums.items())
        nums_con = len(nums) / 3
        ans = []
        for index in range(len(num_tuple)):
            if num_tuple[index][1] > nums_con:
                ans.append(num_tuple[index][0])
        return ans