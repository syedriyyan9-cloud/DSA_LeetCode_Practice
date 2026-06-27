class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        dictChars = {}
        total = 0
        length = len(words)
        for item in chars:
            if item in dictChars:
                dictChars[item] += 1
            else:
                dictChars[item] = 1
        for index in range(length):
            dictWords = {}
            for item in words[index]:
                if item in dictWords:
                    dictWords[item] += 1
                else:
                    dictWords[item] = 1
            valid = True
            for char, value in dictWords.items():
                if char not in dictChars:
                    valid = False
                    break
                if value > dictChars[char]:
                    valid = False
                    break
            if valid:
                total += len(words[index])
        return total