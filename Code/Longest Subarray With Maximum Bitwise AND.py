class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        maxV = max(nums)                                      #The AND of 2 number can only go smaller than either of the 2. So we just need to find the max value and then find the longest subarray which is formed by a consecutive number of max value.
        i, result = 0, 0
        while i < len(nums):
            if nums[i] == maxV:
                j = i
                while j < len(nums) and nums[j] == nums[i]:
                    j += 1
                result = max(result, j - i)
                i = j - 1
            i += 1
        return result
