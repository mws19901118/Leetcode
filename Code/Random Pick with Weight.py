import random
class Solution:

    def __init__(self, w: List[int]):
        self.weightSum = [0]                                                  #Store the cumulative sum for each index; initially, it's 0.
        for i, x in enumerate(w):
            self.weightSum.append(self.weightSum[-1] + x)

    def pickIndex(self) -> int:
        r = random.randint(1, self.weightSum[-1])                             #Random an int in range between 1 and the max cumulative sum.
        start, end = 0, len(self.weightSum)
        while start <= end:                                                   #Do binary search in cumulative sum to find the largest index whose cumulative sum is smaller than the random int.
            mid = (start + end) // 2
            if self.weightSum[mid - 1] < r and self.weightSum[mid] >= r:
                return mid - 1                                                #Return index - 1.
            elif self.weightSum[mid] < r:
                start = mid + 1
            else:
                end = mid - 1


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
