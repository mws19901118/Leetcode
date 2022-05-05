class MyStack:

    def __init__(self):
        self.q = deque()                                            #Use a queue to simulate stack.

    def push(self, x: int) -> None:
        self.q.append(x)                                            #Append x to queue.

    def pop(self) -> int:
        n = len(self.q)                                             #Get current queue length.
        for _ in range(n - 1):                                      #For the first n - 1 elements, popleft then append to queue.
            self.q.append(self.q.popleft())
        return self.q.popleft()                                     #Popleft the last element and return.
        
    def top(self) -> int:
        result = self.pop()                                         #Pop the element at "stack" top.
        self.q.append(result)                                       #Append it to queue again.
        return result                                               #Return result.

    def empty(self) -> bool:
        return not self.q                                           #Return if queue is empty.


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
