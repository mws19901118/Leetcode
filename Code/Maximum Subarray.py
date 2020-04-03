class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        csum, maxsum = -0x7fffffff, -0x7fffffff         #Record the max sum of subarray ending at each element. 
        for i in range(len(nums)):
            csum = max(csum + nums[i], nums[i])         #The max sum of subarray ending at current element equals the greater value of nums[i] and the max sum of subarray ending at previous element plus nums[i].
            maxsum = max(maxsum, csum)                  #If max sum of subarray ending at current element is greater than maxsum, update maxsum.
        return maxsum
