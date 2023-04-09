class RangeModule:

    def __init__(self):
        self.start = []                                                                                                             #Store the range start in ascending order.
        self.end = {}                                                                                                               #Store the range and by range start.

    def addRange(self, left: int, right: int) -> None:
        index = bisect_right(self.start, left)                                                                                      #Binary search the right most place to insert left in self.start.
        if index > 0 and self.end[self.start[index - 1]] >= left:                                                                   #Hanle the case that it has range before it and the previous range overlaps with it.
            right = max(right, self.end[self.start[index - 1]])                                                                     #Update right to be the larger of 2 range end.
            left = min(left, self.start[index - 1])                                                                                 #Update left to be the smaller of 2 range start.
            self.end.pop(self.start[index - 1])                                                                                     #Delete previous range.
            self.start.pop(index - 1)
            index -= 1                                                                                                              #Decrease index.

        self.start.insert(index, left)                                                                                              #Insert left at index and also insert right by left.
        self.end[left] = right
        index += 1                                                                                                                  #Increase index.
        while index < len(self.start) and self.start[index] <= self.end[self.start[index - 1]]:                                     #While the range at index has overlap with inserted range, merge inserted range with overlap range.
            self.end[self.start[index - 1]] = max(self.end[self.start[index - 1]], self.end[self.start[index]])                     #Update the inserted range range to be the overlap range end if it's greater. 
            self.end.pop(self.start[index])                                                                                         #Delete overlap range.
            self.start.pop(index)

    def queryRange(self, left: int, right: int) -> bool:
        index = bisect_right(self.start, left)                                                                                      #Binary search the right most place to insert left in self.start.
        return index > 0 and self.end[self.start[index - 1]] >= right                                                               #If it has range before it and the previous range covers the whole range, return true; otherwise, return false.

    def removeRange(self, left: int, right: int) -> None:
        index = bisect_left(self.start, left)                                                                                       #Binary search the left most place to insert left in self.start.
        if index > 0 and self.end[self.start[index - 1]] > left:                                                                    #Hanle the case that it has range before it and the previous range overlaps with it.
            if self.end[self.start[index - 1]] > right:                                                                             #If the previous range end is greater than right, so it has a right part not removed, insert that range at index.
                self.start.insert(index, right)
                self.end[right] = self.end[self.start[index - 1]]
            self.end[self.start[index - 1]] = left                                                                                  #Set the previous range end to be left.
        while index < len(self.start) and self.end[self.start[index]] <= right:                                                     #While the range at index is fully covered by the to-be-removed range, delete it.
            self.end.pop(self.start[index])
            self.start.pop(index)
        
        if index < len(self.start) and self.start[index] < right:                                                                   #If the range at index is partially covered(always the left part) by the to-be-removed range, update its start.
            self.end[right] = self.end[self.start[index]]
            self.end.pop(self.start[index])
            self.start[index] = right


# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)
