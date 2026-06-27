class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabets = [chr(c) for c in range(97,123)]
        sentence = set(sentence)
        flag = True
        for char in alphabets:
            if char not in sentence:
                flag = False
                break
        if flag:
            return True
        else: 
            return False