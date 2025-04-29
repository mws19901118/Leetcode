class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        result, start, count, max_v = 0, 0, 0, max(nums)    #Initialize result, start of sliding window, count of max value also find the max value.
        for i, x in enumerate(nums):                        #Traverse nums.
            count += x == max_v                             #Update count.
            while count >= k:                               #While count is greater than or equal to k, move forward start and update count.
                count -= nums[start] == max_v
                start += 1
            result += start                                 #Now, for all subarrays starting in nums[:start] and ending at x will have at least k max value.
        return result
