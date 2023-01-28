class SummaryRanges:

    def __init__(self):
        self.intervals = []                                                                                                                                     #Store intervals.
        self.inserted = set()                                                                                                                                   #Store inserted number.

    def addNum(self, value: int) -> None:
        if value in self.inserted:                                                                                                                              #If value is already inserted, directly return.
            return
        self.inserted.add(value)                                                                                                                                #Add value to inserted.
        index = bisect.bisect_left(self.intervals, [value, value])                                                                                              #Find index to insert [value, value] in intervals.
        if index > 0 and self.intervals[index - 1][1] == value - 1 and (index == len(self.intervals) or self.intervals[index][0] > value + 1):                  #If there is an interval on the left, merge with it.
            self.intervals[index - 1][1] = value
        elif index < len(self.intervals) and self.intervals[index][0] == value + 1 and (index == 0 or self.intervals[index - 1][1] < value - 1):                #If there is an interval on the right, merge with it.
            self.intervals[index][0] = value
        elif index > 0 and self.intervals[index - 1][1] == value - 1 and index < len(self.intervals) and self.intervals[index][0] == value + 1:                 #If there are both intervals on two sides, merge them and delete one of them.
            self.intervals[index - 1][1] = self.intervals[index][1]
            del self.intervals[index]
        else:                                                                                                                                                   #Otherwise, insert [value, value] at index.
            self.intervals.insert(index, [value, value])

    def getIntervals(self) -> List[List[int]]:                                                                                                                  #Return intervals.
        return self.intervals


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()
