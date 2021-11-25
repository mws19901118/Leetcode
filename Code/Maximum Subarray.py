class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result, currentMax = float('-inf'), 0           #Initialize result and the max sum of subarray ending at current number. 
        for x in nums:                                  #Traverse nums.
            currentMax = max(x, currentMax + x)         #The max sum of subarray ending at current number equals the greater value of x and the max sum of subarray ending at previous element plus x.
            result = max(result, currentMax)            #If max sum of subarray ending at current number is greater than result, update result.
        return result
