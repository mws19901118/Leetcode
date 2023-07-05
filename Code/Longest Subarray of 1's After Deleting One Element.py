class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        lastZeroIndex, secondLastZeroIndex, result = -1, -2, 0                #Initialize the last index and second last index of zero as well as result.
        for i in range(len(nums) + 1):                                        #Traverse nums.
            if i == len(nums) or nums[i] == 0:                                #If reaches the end or nums[i] is 0, calculate the longest subarray of 1's after deleting the zero at lastZeroIndex.
                result = max(result, i - secondLastZeroIndex - 2)             #Length of subarray is i - lastZeroIndex - 1 + lastZeroIndex - secondLastZeroIndex - 1, which is i - secondLastZeroIndex - 2.
                lastZeroIndex, secondLastZeroIndex = i, lastZeroIndex         #Update lastZeroIndex and secondLastZeroIndex.
        return result if result < len(nums) else result - 1                   #If result equals to length of nums, all numbers in nums is 1 so return result - 1; otherwise return result.
