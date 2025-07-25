class Solution:
    def maxSum(self, nums: List[int]) -> int:
        max_v = max(nums)                                                            #Get the max value of nums.
        return max_v if max_v <= 0 else sum(x for x in set(nums) if x > 0)           #If max value is not greater than 0, just return the max value; otherwise, return the sum of unique positive elements.
