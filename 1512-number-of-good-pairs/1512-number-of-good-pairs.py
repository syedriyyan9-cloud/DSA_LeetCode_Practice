class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # done in week 1 - using arrays
        # count = 0
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] == nums[j]:
        #             count += 1
        # return count

        # done in week 3 - using hashmaps
        count = 0
        map_nums = {}
        for item in nums:
            if item in map_nums:
                count += map_nums.get(item)
                map_nums[item] += 1
            else:
                map_nums[item] = 1
        return count
