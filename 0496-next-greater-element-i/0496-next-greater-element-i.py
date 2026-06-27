class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dictN2 = {}
        ans = []
        for index, item in enumerate(nums2):
            dictN2[item] = index
        length = len(nums2)
        for index in range(len(nums1)):
            if nums1[index] in dictN2:
                num = dictN2.get(nums1[index])
                for s_index in range(num, length):
                    if nums2[s_index] > nums1[index]:
                        ans += [nums2[s_index]]
                        break
                else:
                    ans += [-1]
        return ans