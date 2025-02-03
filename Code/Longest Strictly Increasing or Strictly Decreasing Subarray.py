class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        result = 1                                                          #Initialize result.
        i = 0                                                               #Initialize pointer.
        while i < len(nums):                                                #Iterate while i hasn't reaching the end.
            j = i + 1                                                       #Initialize j to be i + 1.
            if j == len(nums) or nums[i] == nums[j]:                        #If j is beyond the end or nums[j] equals nums[i], move i to j and continue.
                i = j
                continue
            sign = 1 if nums[j] > nums[i] else -1                           #Get the sign if nums[j] is increasing or decreasing compared to nums[i].
            while j < len(nums) and (nums[j] - nums[j - 1]) * sign > 0:     #Move forward j while the nums[i:j + 1] is strictly increasing or decreasing.
                j += 1
            result = max(result, j - i)                                     #Update result if j - i is greater.
            i = j - 1                                                       #Move i to j - 1.
        return result
