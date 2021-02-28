class FreqStack:
    def __init__(self):
        self.counts = defaultdict(int)                                    #Store the count of each element.
        self.values = defaultdict(list)                                   #Store the elements at each count in the order of pushing to stack.
        self.maxFrequency = 0                                             #Maintain the max frequency so far.
        
    def push(self, x: int) -> None:
        self.counts[x] += 1                                               #Update count of x.
        self.values[self.counts[x]].append(x)                             #Append x to the list of elements having same count of x.
        self.maxFrequency = max(self.maxFrequency, self.counts[x])        #Update max frequency.

    def pop(self) -> int:
        x = self.values[self.maxFrequency].pop()                          #Pop value from the list of elements having the max frequency.
        if len(self.values[self.maxFrequency]) == 0:                      #Update max frequency if no element left at current max frequency.
            self.maxFrequency -= 1
        self.counts[x] -= 1                                               #Update count of x.
        return x                                                          #Return x.

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()
