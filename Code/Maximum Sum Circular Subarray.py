class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        maxSumTowardsEnd, cSum = [0], 0
        for i in reversed(range(len(A))):                                                                   #Find the max sum from each element to the end of list(must include the end).
            cSum += A[i]
            maxSumTowardsEnd.append(max(maxSumTowardsEnd[-1], cSum))
        maxSum, minSumFromBeginning, cSum = -30001, 0, 0
        for i in range(len(A)):
            cSum += A[i]                                                                                    #Calculate cumulative sum/
            maxSum = max(maxSum, cSum - minSumFromBeginning, cSum + maxSumTowardsEnd[len(A) - 1 - i])       #For each element, find max sum of sub arraies which ends at current element, across the beginning and not across the beginning.
            minSumFromBeginning = min(minSumFromBeginning, cSum)
        return maxSum
