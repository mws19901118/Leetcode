class MyQueue:

    def __init__(self):
        self.forward = []                                                       #Store elements in original order of pushing to queue.
        self.backward = []                                                      #Store elements in riversed order of pushing to queue.

    def push(self, x: int) -> None:
        self.forward.append(x)                                                  #Push x to the forward stack.

    def pop(self) -> int:
        self.peek()                                                             #Peek the queue.
        return self.backward.pop()                                              #Pop the last element in backward stack and return.

    def peek(self) -> int:
        if not self.backward:                                                   #If the backward stack is empty, pop each element from the forward stack and push them to the backward stack.
            while self.forward:
                self.backward.append(self.forward.pop())
        return self.backward[-1]                                                #Return the top of backward stack.

    def empty(self) -> bool:
        return not self.forward and not self.backward                           #Return true if both forward stach and backward are empty.


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
