class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if not n:                                                                     #If n is 0, return 0.
            return 0
        nums = [0] * (n + 1)
        nums[1] = 1
        result = 1
        for i in range(2, n + 1):
            nums[i] = nums[i // 2] + nums[i // 2 + 1] if i & 1 else nums[i // 2]      #Generate array.
            result = max(nums[i], result)                                             #Update max value.
        return result
