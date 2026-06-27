class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set_n1 = set(nums1)
        set_n2 = set(nums2)
        ans = []
        count = 0
        for item in nums1:
            if item in set_n2:
                count += 1
        ans += [count]
        count = 0
        for item in nums2:
            if item in set_n1:
                count += 1
        ans += [count]
        count = 0
        return ans