class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []
        for index in range(1, n + 1):
            if index % 3 == 0  and index % 5 == 0:
                answer += ["FizzBuzz"]
            elif index % 3 == 0:
                answer += ["Fizz"]
            elif index % 5 == 0:
                answer += ["Buzz"]
            else:
                answer += [str(index)]
        return answer