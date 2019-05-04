class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()                           #Sort nums.
        pairSum = 0                           #Add all elements in odd indexes.
        for i in range(0, len(nums), 2):
            pairSum += nums[i]
        return pairSum
