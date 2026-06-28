class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dictarr = {}
        answer = True
        for item in arr:
            if item in dictarr:
                dictarr[item] = dictarr[item] + 1
            else:
                dictarr[item] = 1
        arr_list = [v for v in dictarr.values()]
        for index in range(len(arr_list)):
            for s_index in range(index + 1, len(arr_list)):
                if arr_list[index] == arr_list[s_index]:
                    answer = False
                    break
        return answer
        