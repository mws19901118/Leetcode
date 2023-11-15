class MovingAverage:

    def __init__(self, size: int):
        self.n = size                                        #Store size.
        self.s = 0                                           #Store sum.
        self.q = deque()                                     #Sotre numbers in queue.

    def next(self, val: int) -> float:
        self.q.append(val)                                   #Append val to queue.
        self.s += val                                        #Add val to sum.
        if len(self.q) > self.n:                             #If the length of q is greater than size, popleft from queue and substract it from sum.
            self.s -= self.q.popleft()
        return self.s / len(self.q)                          #Calculate the average and return.

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
