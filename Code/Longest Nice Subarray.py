class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        used, start, result = 0, 0, 0              #Initialize used bits, start of window and result.
        for i, x in enumerate(nums):               #Traverse nums.
            while used & x:                        #While used bits have shared bits with current number, remove bits of nums[start] by doing xor and increase start.
                used ^= nums[start]
                start += 1
            result = max(result, i - start + 1)    #Now, nums[start:i + 1] is the longest nice subarray ending at i, so update result if necessary.
            used |= x                              #Add bits of x to used bits.
        return result
