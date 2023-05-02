class Solution:
    def arraySign(self, nums: List[int]) -> int:
        if any(x == 0 for x in nums):                                     #If any number is 0, return 0.
            return 0
        negativeCount = sum(1 for x in nums if x < 0)                     #Count negative numbers.
        return -1 if negativeCount & 1 else 1                             #Return -1 if negativeCount is odd; otherwise return 1.
