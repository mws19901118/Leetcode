class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        total_sum, prefix_sum, count = sum(nums), 0, 0          #Calculate total sum and initialize prefix sum and count.
        for i in range(len(nums) - 1):                          #Traverse nums except the last number.
            prefix_sum += nums[i]                               #Add nums[i] to prefix sum.
            count += int(prefix_sum >= total_sum - prefix_sum)  #Increase count if split at i is valid.
        return count
