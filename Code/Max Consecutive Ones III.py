class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        start, count, length = 0, 0, 0                    #Initialize the start of sliding window, count of 0 and max length.
        for i, x in enumerate(nums):                      #Traverse nums.
            count += 1 - x                                #Increase count of zero if necessary.
            while count > k:                              #While count of zero is greater than k, move start forward.
                count -= 1 - nums[start]
                start += 1
            length = max(length, i - start + 1)           #Now, we can flip all zeros in window and make the window consecutive ones. Update length if necessary.
        return length
