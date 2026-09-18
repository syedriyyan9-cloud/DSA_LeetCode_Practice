class Solution:
    def isHappy(self, n: int) -> bool:
        summ = n
        tries = 0
        while summ != 1 and tries != 20:
            digits = str(summ)
            square = 0
            for digit in digits:
                square += int(digit) ** 2
            summ = square
            tries += 1
        if summ == 1:
            return True
        else:
            return False