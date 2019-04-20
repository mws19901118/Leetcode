import random
class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects                                                                          #Store the rectangles.
        self.prefixSum = [0]                                                                        #Use a list to store the prefix sum of integer points count of each rectangle.
        for r in rects:
            self.prefixSum.append(self.prefixSum[-1] + (r[2] - r[0] + 1) * (r[3] - r[1] + 1))

    def pick(self) -> List[int]:
        total = self.prefixSum[-1]                                                                  #Get the total count of integer points.
        randomInt = random.randint(1, total)                                                        #Random an integer.
        index = -1
        start, end = 1, len(self.prefixSum) - 1                                                     #Binary search which rectangle the random int belongs to. Because the first element in prefix sum does not belongs to any rectangle, we start from 1.
        while start <= end:
            mid = (start + end) // 2
            if self.prefixSum[mid - 1] < randomInt and self.prefixSum[mid] >= randomInt:
                index = mid - 1                                                                     #Get the index of rectangle, which is mid - 1.
                break
            elif self.prefixSum[mid - 1] >= randomInt:
                end = mid - 1
            else:
                start = mid + 1
            
        offset = randomInt - self.prefixSum[index] - 1                                              #Calculate the offset of random int in rectangle. If we consider the rectangle as a list of integer points, starting from bottom left, going right first then up, until top right. Offset is the index of integer point in list.
        px = self.rects[index][0] + offset % (self.rects[index][2] - self.rects[index][0] + 1)      #Calculate px based on offset.
        py = self.rects[index][1] + offset // (self.rects[index][2] - self.rects[index][0] + 1)     #Calculate px based on offset.
        return [px, py]

# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()
