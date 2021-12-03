class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minp, maxp, result = 1, 1, -math.inf                                        #Initialize the min product and max product at each index and result as well.
        for x in nums:                                                              #Traverse nums.
            minp, maxp = min(minp * x, maxp * x, x), max(minp * x, maxp * x, x)     #Update the min product and max product at each index.
            result = max(maxp, result)                                              #Update result.
