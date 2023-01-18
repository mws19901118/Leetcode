class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        maxSumTowardsEnd, cSum = [0], 0
        for i in reversed(range(len(nums))):                                                                   #Find the max sum from each element to the end of list(must include the end).
            cSum += nums[i]
            maxSumTowardsEnd.append(max(maxSumTowardsEnd[-1], cSum))
        maxSum, minSumFromBeginning, cSum = -30001, 0, 0
        for i in range(len(nums)):
            cSum += nums[i]                                                                                    #Calculate cumulative sum.
            maxSum = max(maxSum, cSum - minSumFromBeginning, cSum + maxSumTowardsEnd[len(nums) - 1 - i])       #For each element, find max sum of sub arraies which ends at current element, across the beginning and not across the beginning.
            minSumFromBeginning = min(minSumFromBeginning, cSum)
        return maxSum
