class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dictNums = {}
        for num in nums:
            if num in dictNums:
                dictNums[num] = dictNums[num] + 1
            else:
                dictNums[num] = 1
        m_element = max(dictNums, key=dictNums.get)
        return m_element