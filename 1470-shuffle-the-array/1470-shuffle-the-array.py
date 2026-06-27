class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        index = 0
        array = []
        while index < n:
            array += [nums[index]]
            array += [nums[index + n]]
            index += 1
        return array
        