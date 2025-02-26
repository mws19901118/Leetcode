class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        result, max_sum, min_sum, prefix_sum = 0, 0, 0, 0                                        #Initialize result, max prefix sum, min prefix sum and current prefix sum.
        for x in nums:                                                                           #Traverse nums.
            prefix_sum += x                                                                      #Add x to prefix sum.
            result = max(result, abs(prefix_sum - min_sum), abs(prefix_sum - max_sum))           #Update result if either abs(prefix_sum - min_sum), the current largest subarry sum or abs(prefix_sum - max_sum), current smallest subarray sum is larger.
            max_sum, min_sum = max(prefix_sum, max_sum), min(prefix_sum, min_sum)                #Update max prefix sum and min prefix sum.
        return result
