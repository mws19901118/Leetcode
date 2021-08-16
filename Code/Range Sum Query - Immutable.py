class NumArray:

    def __init__(self, nums: List[int]):
        self.accumulateSum = [0]                                                #Initialize accumulate sum with 0.
        self.accumulateSum.extend(list(accumulate(nums)))                       #Compute accumulate sum.

    def sumRange(self, left: int, right: int) -> int:
        return self.accumulateSum[right + 1] - self.accumulateSum[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
