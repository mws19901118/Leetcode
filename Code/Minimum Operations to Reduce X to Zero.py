class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        prefixSumMap = {0: -1}                                                                #Store prefix sum and its index, initially it is 0 at -1.
        result, prefixSum, target = len(nums) + 1, 0, sum(nums) - x                           #Initialize result and prefixSum as well as target. Since we want to find the minimum x + y so that nums[:x] + nums[-y:] == x, it is same as find the longest subarray which sums up at sum(nums) - x.
        for i, x in enumerate(nums):                                                          #Traverse nums.
            prefixSum += x                                                                    #Updte prefixSum.
            prefixSumMap[prefixSum] = i                                                       #Set the index of current prefixSum in map.
            if prefixSum - target in prefixSumMap:                                            #If prefixSum - target is in map, we found a subarray that satisfies the requirement and its length is i - prefixSumMap[prefixSum - target].
                result = min(result, len(nums) - i + prefixSumMap[prefixSum - target])        #Then update result if len(nums) - (i - prefixSumMap[prefixSum - target]) is smaller.
        return result if result < len(nums) + 1 else -1                                       #Return -1 if result is still len(nums) + 1 as we cannot find such subarray; otherwise, return result.
