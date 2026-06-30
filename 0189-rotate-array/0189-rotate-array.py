class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # for _ in range(k):
        #     last_element = nums[-1]
        #     for index in range(len(nums) - 1, 0, -1):
        #         nums[index] = nums[index - 1]
        #     nums[0] = last_element
        for _ in range(k):
            last = nums.pop()
            nums.insert(0, last)
        # r = len(nums) - 1
        # while k > 0:
        #     temp = nums[r]
        #     for index in range(len(nums)-1, -1, -1):
        #         if index == 0:
        #             nums[index] = temp
        #         else:
        #             nums[index] = nums[index-1]
        #     k -= 1
        # return nums