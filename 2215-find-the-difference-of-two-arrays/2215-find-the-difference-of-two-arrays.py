class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)
        main_set = set(nums1 + nums2)
        answer = [[],[]]
        for item in main_set:
            if item in set1 and item in set2:
                set1.discard(item)
                set2.discard(item)
        answer[0] += set1
        answer[1] += set2
        return answer