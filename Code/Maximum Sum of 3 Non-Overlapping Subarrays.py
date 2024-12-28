class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        prefixSum = [0]                                                                                              #Build prefix sum first.
        for x in nums:
            prefixSum.append(prefixSum[-1] + x)
        @cache                                                                                                       #Cache result.
        def dp(index: int, count: int) -> (int, List[int]):                                                          #DP to find the max sum and indexes in nums[index:] for given count of non overlapping k length subarraies.
            if not count or index + count * k > len(nums):                                                           #If count is 0 or the remaining list cannot be split to given count of non overlapping k length subarraies, return 0 and empty list.
                return 0, []
            notStartAtCurrentSum, notStartAtCurrentSumIndexes = dp(index + 1, count)                                 #DP to find the sum and indexes of not starting at current number.
            startAtCurrentSum, startAtCurrentIndexes = dp(index + k, count - 1)                                      #DP to find the next sum and indexes after a subarray starting at current number.
            if notStartAtCurrentSum > startAtCurrentSum + prefixSum[index + k] - prefixSum[index]:                   #If not start at current will yield higher sum, return sum and indexes of not starting at current number.
                return notStartAtCurrentSum, notStartAtCurrentSumIndexes
            else:                                                                                                    #Otherwise, calculate the sum and indxes starting at current number and return.
                return startAtCurrentSum + prefixSum[index + k] - prefixSum[index], [index] + startAtCurrentIndexes
        
        return dp(0, 3)[1]                                                                                           #Return the indexes of dp(0, 3).
