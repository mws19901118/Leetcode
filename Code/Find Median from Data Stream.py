import heapq
class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.left = []                                                      #Maintain a max heap of the left half.
        self.right = []                                                     #Maintain a min heap of the right half.
        

    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        if len(self.right) == 0:                                            #If the right half is empty, push it to the right half.
            heapq.heappush(self.right, num)
        else:                                                               #If it's not smaller than the min value of right half, push it to the right half.
            if num >= self.right[0]:
                heapq.heappush(self.right, num)
            else:                                                           #Otherwise push its opposite number to the left half.
                heapq.heappush(self.left, -num)
        if len(self.left) - len(self.right) > 1:                            #Maintain the lengths of left half and right half balanced(difference between 2 lengths no larger than 1).
            t = heapq.heappop(self.left)
            heapq.heappush(self.right, -t)
        if len(self.right) - len(self.left) > 1:
            t = heapq.heappop(self.right)
            heapq.heappush(self.left, -t)
    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        if len(self.right) > len(self.left):                                #If the length of right half is larger than that of left half, the total length is odd, return the min value of right half.
            return self.right[0]
        elif len(self.left) > len(self.right):                              #If the length of left half is larger than that of right half, the total length is odd, return the max value of left half.
            return -self.left[0]
        else:                                                               #Otherwise, the total length is even, return the mean of the min value of right half and the max value of left half.
            return (self.right[0] - self.left[0]) * 1.0 / 2

# Your MedianFinder object will be instantiated and called as such:
# mf = MedianFinder()
# mf.addNum(1)
# mf.findMedian()
