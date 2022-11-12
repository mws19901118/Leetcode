class MedianFinder:
    def __init__(self):
        self.left = []                                                                                          #Maintain a max heap of the left half.
        self.right = []                                                                                         #Maintain a min heap of the right half.

    def addNum(self, num: int) -> None:
        if len(self.right) == 0 or num >= self.right[0]:                                                        #If the right half is empty or it's not smaller than the min value of right half, push it to the right half.
            heapq.heappush(self.right, num)
        else:                                                                                                   #Otherwise push its opposite number to the left half.
            heapq.heappush(self.left, -num)
        if len(self.left) - len(self.right) >= 1:                                                               #Maintain the lengths of left half and right half balanced and always keep the right half no shorter than the left half.
            t = heapq.heappop(self.left)
            heapq.heappush(self.right, -t)
        elif len(self.right) - len(self.left) > 1:
            t = heapq.heappop(self.right)
            heapq.heappush(self.left, -t)
            
    def findMedian(self) -> float:
        return self.right[0] if len(self.right) > len(self.left) else (self.right[0] - self.left[0]) / 2        #If right half is longer, return the min value of right half; otherwise return the mean of the min value of right half and the max value of left half.

# Your MedianFinder object will be instantiated and called as such:
# mf = MedianFinder()
# mf.addNum(1)
# mf.findMedian()
