class RLEIterator:

    def __init__(self, A: List[int]):
        self.encode = A                                                           #Store the encode.
        self.index = 0                                                            #Store the index.

    def next(self, n: int) -> int:
        while self.index < len(self.encode) and self.encode[self.index] < n:      #While the current number count is smaller than n, subtract n by current number count and go to next number.
            n -= self.encode[self.index]
            self.index += 2
        if self.index >= len(self.encode):                                        #If reaches the end, return -1.
            return -1
        self.encode[self.index] -= n                                              #Subtract current number count by n.
        return self.encode[self.index + 1]                                        #Return current number, the next element after index.

# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(A)
# param_1 = obj.next(n)
