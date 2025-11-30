class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        prefixSum, result, remainder = 0, len(nums), sum(nums) % p      #Initialize prefix sum, result and calculate the remainder of overall sum divided by p.
        if not remainder:                                               #If no remainder, directly return 0.
            return 0
        lastIndex = {0: -1}                                             #Initialize the last index i of remaidner x such that sum(nums[:i + 1]) % p == x; initially the lastIndex of 0 is -1.
        for i, x in enumerate(nums):                                    #Traverse nums.
            prefixSum += x                                              #Update prefix sum.
            target = (prefixSum % p - remainder) % p                    #Calculate the target remainder, while is (prefixSum % p - remainder) % p.
            if target in lastIndex:                                     #If it exists, let's say the index is j, then the sum of the rest of array, sum(nums) - (sum(nums[:i + 1]) - sum(nums[:j + 1]), can be divided by p.
                result = min(result, i - lastIndex[target])             #So, we need the largest j to minimize i - j.
            lastIndex[prefixSum % p] = i                                #Update the last index if prefixSum % p to i.
        return result if result < len(nums) else -1                     #If result is smaller than len(nums), return it; otherwise return -1 because cannot remove the entire array,
