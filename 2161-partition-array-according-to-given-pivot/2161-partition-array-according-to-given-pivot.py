class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        nums1 = nums[:]
        s, f = 0, 0
        for index in range(len(nums)):
            if nums1[f] < pivot:
                nums1[s] = nums1[f]
                s += 1
                f += 1
            else:
                f += 1
        smaller = nums1[:s]
        nums1 = nums[:]
        s, f = 0, 0
        for index in range(len(nums)):
            if nums1[f] > pivot:
                nums1[s] = nums1[f]
                s += 1
                f += 1
            else: 
                f += 1
        larger = nums1[:s]
        middle = [x for x in nums if x == pivot]
        nums = smaller + middle + larger
        return nums