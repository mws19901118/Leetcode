class Solution:

    def __init__(self, w: List[int]):
        self.weightSum = [0]                                                  #Store the cumulative sum for each index; initially, it's 0.
        for i, x in enumerate(w):
            self.weightSum.append(self.weightSum[-1] + x)

    def pickIndex(self) -> int:
        r = random.randint(1, self.weightSum[-1])                             #Random an int in range between 1 and the max cumulative sum.
        return bisect_right(self.weightSum, r) - 1                            #Do binary search in cumulative sum to find the largest index whose cumulative sum is smaller than the random int. and return the index - 1.

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
