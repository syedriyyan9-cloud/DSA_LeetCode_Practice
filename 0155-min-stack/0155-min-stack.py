class MinStack:

    def __init__(self):
        self.stack = list()
        self.cpy = self.stack.copy()

    def push(self, value: int) -> None:
        self.stack.append(value)
        self.cpy.append(value)
        self.cpy.sort(reverse=True)

    def pop(self) -> None:
        value = self.stack.pop()
        self.cpy.remove(value)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.cpy[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()