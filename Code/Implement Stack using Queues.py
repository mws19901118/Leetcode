class MyStack:

    def __init__(self):
        self.q = deque()                                            #Use a queue to simulate stack.
        self.stackTop = None                                        #Store the top of stack,
        self.length = 0                                             #Store size of stack.

    def push(self, x: int) -> None:
        self.q.append(x)                                            #Append x to queue.
        self.stackTop = x                                           #Update stack top and length.
        self.length += 1

    def pop(self) -> int:
        for _ in range(self.length - 1):                            #Popleft self.length - 1 elements then push them back to queue and update stack top.
            self.stackTop = self.q.popleft()
            self.q.append(self.stackTop)
        self.length -= 1                                            #Update length.
        return self.q.popleft()                                     #Popleft the last element and return.
        
    def top(self) -> int:                                           #Return stack top.
        return self.stackTop

    def empty(self) -> bool:                                        #Return self.length.
        return not self.length

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
