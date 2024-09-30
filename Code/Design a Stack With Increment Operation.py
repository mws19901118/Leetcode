class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = [0] * maxSize                                                    #Initialize stack with fixed length.
        self.increamental = [0] * maxSize                                             #Initialize increment at each index with 0.
        self.index = -1                                                               #Initialize the current index of stack top.

    def push(self, x: int) -> None:
        if self.index < len(self.stack) - 1:                                          #If stack top is not the end, increase index and put x at index.
            self.index += 1
            self.stack[self.index] = x

    def pop(self) -> int:
        if self.index < 0:                                                            #If stack is empty, return -1.
            return -1
        result = self.stack[self.index] + self.increamental[self.index]               #The current value at stack top is self.stack[self.index] + self.increamental[self.index].
        self.index -= 1                                                               #Decrease index.
        if self.index >= 0:                                                           #If index is not smaller than 0, add self.increamental[self.index + 1] to self.increamental[self.index], because self.stack[index] should also be affected by the increment.
            self.increamental[self.index] += self.increamental[self.index + 1]
        self.increamental[self.index + 1] = 0                                         #Reset self.incremental[self.index + 1].
        return result

    def increment(self, k: int, val: int) -> None:
        if self.index >= 0:                                                           #If stack is not empty, increase val at the index of min(self.index, k - 1).
            self.increamental[min(self.index, k - 1)] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
