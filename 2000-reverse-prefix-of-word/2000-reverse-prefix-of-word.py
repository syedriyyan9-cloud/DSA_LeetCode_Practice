class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        end = 0
        word_list = 0
        for i in range(len(word)):
            if word[i] == ch:
                word_list = list(word[:i+1])
                s = 0
                f = i
                end = i
                break
        else:
            return word
        while s < f:
            word_list[s], word_list[f] = word_list[f], word_list[s]
            s += 1
            f -= 1
        return "".join(word_list) + word[end+1:] 