class NumberContainers:

    def __init__(self):
        self.numbers = {}                                                          #Store number on each index.
        self.indexes = defaultdict(SortedList)                                     #For each number, store its indexes in a sorted list.

    def change(self, index: int, number: int) -> None:
        if index in self.numbers:                                                  #If there is a number on index, discard index from its indexes sorted list.
            self.indexes[self.numbers[index]].discard(index)
        self.numbers[index] = number                                               #Set number on current index.
        self.indexes[number].add(index)                                            #Add index to the indexes sorted list of current number.

    def find(self, number: int) -> int:
        return self.indexes[number][0] if len(self.indexes[number]) else -1        #If current number doesn't have indexes, return -1; otherwise return its first index.

# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)
