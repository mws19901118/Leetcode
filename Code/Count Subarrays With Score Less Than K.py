class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        result, start, window_sum = 0, 0, 0              #Initialize result, start of sliding window and window sum.
        for i, x in enumerate(nums):                     #Traverse nums.
            window_sum += x                              #Add x to window and update window sum.
            score = window_sum * (i - start + 1)         #Calculate score.
            while score >= k:                            #While score is greater than or equal to k, move forward start.
                window_sum -= nums[start]                #Deduct nums[start] from window sum.
                start += 1
                score = window_sum * (i - start + 1)     #Re-calculate the score.
            result += i - start + 1                      #Now every subarray starting at nums[start:i + 1] and ending at i will have a score smaller than k, because k will only decrease while the window shrinks.
        return result
