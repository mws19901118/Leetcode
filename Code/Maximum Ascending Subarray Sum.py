class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        result, i = 0, 0                                      #Initialize result and an index pointer.
        while i < len(nums):                                  #Traverse nums.
            j = i + 1
            s = nums[i]                                       #Initialize sum for current ascending subarray.
            while j < len(nums) and nums[j] > nums[j - 1]:    #Calculate the sum of current ascending subarray until it stops.
                s += nums[j]
                j += 1
            result = max(result, s)                           #Update result.
            i = j
        return result
