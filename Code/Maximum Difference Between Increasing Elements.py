class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        min_v, result = inf, 0                  #Initialize min value and result.
        for x in nums:                          #Traverse nums.
            result = max(result, x - min_v)     #Update result if the diff between current number and min value is larger.
            min_v = min(min_v, x)               #Update the min value of traversed numbers.
        return result if result > 0 else -1     #Return result if result is greater than 0; otherwise, return -1.
