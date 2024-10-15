class FirstUnique:

    def __init__(self, nums: List[int]):
        self.queue = deque(nums)                                        #Initialize queue.
        self.isDuplicate = {}                                           #Add use a dictionary 
        for x in nums:                                                  #Process initial input. 
            if x not in self.isDuplicate:
                self.isDuplicate[x] = False
            else:
                self.isDuplicate[x] = True
        self.nextUnique()                                               #Move out duplicate in front of the queue.

    def nextUnique(self) -> None:
        while self.queue and self.isDuplicate[self.queue[0]]:           #Popleft queue until the top of queue is unique.
            self.queue.popleft()

    def showFirstUnique(self) -> int:
        return -1 if not self.queue else self.queue[0]                  #Return -1 if queue is empty; otherwise return top of queue.

    def add(self, value: int) -> None:
        if value not in self.isDuplicate:                               #If value is not seen, append it to queue and mark it as no-duplicate.
            self.queue.append(value)
            self.isDuplicate[value] = False
        elif not self.isDuplicate[value]:                               #Otherwise, mark it as duplicate.
            self.isDuplicate[value] = True
        self.nextUnique()                                               #Move out duplicate in front of the queue.

# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
