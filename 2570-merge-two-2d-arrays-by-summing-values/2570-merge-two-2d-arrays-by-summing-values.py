class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        x, y = 0,0
        new_list = []
        while x < len(nums1) or y < len(nums2):
            if x == len(nums1) and y == len(nums2):
                break
            elif x >= len(nums1):
                new_list.append(nums2[y])
                y += 1
            elif y >= len(nums2):
                new_list.append(nums1[x])
                x += 1
            elif nums1[x][0] > nums2[y][0]:
                new_list.append(nums2[y])
                y += 1
            elif nums2[y][0] > nums1[x][0]:
                new_list.append(nums1[x])
                x += 1
            elif nums1[x][0] == nums2[y][0]:
                new_list.append([nums1[x][0], nums1[x][1] + nums2[y][1]])
                x += 1
                y += 1
        return new_list