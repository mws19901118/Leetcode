class MaxStack:

    def __init__(self):
        self.stack = []                                                             #Store the values in stack.
        self.heap = []                                                              #Store the values in a max heap.
        self.id = 0                                                                 #Assign each value a self incremental id.
        self.removed = set()                                                        #Store the ids of values that are poped out.

    def push(self, x: int) -> None:
        heapq.heappush(self.heap, (-x, -self.id))                                   #Push x and its id in max heap.
        self.stack.append((x, self.id))                                             #Append x and its id in stack.
        self.id += 1                                                                #Increase id.

    def pop(self) -> int:
        while self.stack and self.stack[-1][1] in self.removed:                     #While stack is not empty and top of stack is already removed, pop stack.
            self.stack.pop()
        x, id = self.stack.pop()                                                    #Pop value at top of stack and its id.
        self.removed.add(id)                                                        #Add id to removed set.
        return x                                                                    #Return value.

    def top(self) -> int:
        while self.stack and self.stack[-1][1] in self.removed:                     #While stack is not empty and top of stack is already removed, pop stack.
            self.stack.pop()
        return self.stack[-1][0]                                                    #Return the value at top of stack.

    def peekMax(self) -> int:
        while self.heap and -self.heap[0][1] in self.removed:                       #While heap is not empty and top of heap is already popped out, pop stack.
            heapq.heappop(self.heap)
        return -self.heap[0][0]                                                     #Return the value at top of heap.

    def popMax(self) -> int:
        while self.heap and -self.heap[0][1] in self.removed:                       #While heap is not empty and top of heap is already popped out, pop stack.
            heapq.heappop(self.heap)
        x, id = heapq.heappop(self.heap)                                            #Pop value at top of heap and its id.
        self.removed.add(-id)                                                       #Add id to remove set.
        return -x                                                                   #Return value.
        


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
