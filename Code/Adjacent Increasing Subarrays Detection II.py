class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        currLength, prevLength, result = 1, 0, 0                                  #Initialize currLength of current strictly increasing subarray, previous strictly increasing subarray, and result.
        for i in range(1, len(nums)):                                             #Traverse from 1 to len(nums) - 1.
            if nums[i] > nums[i - 1]:                                             #If nums[i] > nums[i - 1], increase currLength.
                currLength += 1
            else:                                                                 #Otherwise, set prevLength to currLength and reset currLength to 1.
                prevLength, currLength = currLength, 1
            result = max(result, min(prevLength, currLength), currLength // 2)    #Previous subarray and current subarray can make an adjacent pair; we can also divide current subarray to 2 parts. Take the max of min length in each case and update result if necessary.
        return result
