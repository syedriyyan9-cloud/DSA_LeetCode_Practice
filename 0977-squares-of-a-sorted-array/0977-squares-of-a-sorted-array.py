class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squared_list = [x**2 for x in nums]
        squared_list.sort()
        return squared_list