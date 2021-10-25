class MinStack:

    def __init__(self):
        self.valueStack = []
        self.minStack = []

    def push(self, x: int) -> None:
        self.valueStack.append(x)                               #Append x to valueStack.
        if not self.minStack or x <= self.minStack[-1]:         #If minStack is empty or x <= current min, push x into minstack.
            self.minStack.append(x)

    def pop(self) -> None:
        if self.valueStack[-1] == self.minStack[-1]:            #If top of valueStack eqauls top of minStack, pop minStack.
            self. minStack.pop()
        self.valueStack.pop()                                   #Pop valueStack.

    def top(self) -> int:
        return self.valueStack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
