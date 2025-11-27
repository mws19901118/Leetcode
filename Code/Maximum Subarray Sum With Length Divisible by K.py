class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        prefixSum, result = 0, -inf                                                    #Initialize prefix sum and result.
        minPrefixSum = [0] + [inf] * (k - 1)                                           #Initialize the min prefix sum at each index plus 1 then divided by k. Since initially perfix sum is 0, so minPrefixSum[0] = 0. 
        for i, x in enumerate(nums):                                                   #Traverse nums.
            prefixSum += x                                                             #Update prefix sum.
            result = max(result, prefixSum - minPrefixSum[(i + 1 - k) % k])            #For the subarray ending at current index whose length is divisible by k, the max subarray sum is prefixSum - minPrefixSum[(i + 1 - k) % k].
            minPrefixSum[(i + 1) % k] = min(minPrefixSum[(i + 1) % k], prefixSum)      #Update minPrefixSum[(i + 1) % k]. 
        return result
