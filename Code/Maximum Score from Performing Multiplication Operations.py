class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        m = len(multipliers)                                                                                            #Get the length of multipliers.
        dp = [0 for _ in range(m + 1)]                                                                                  #Initialize the dp array for length m + 1. For each iteration l, dp[i] means the max score for taking x numbers from front and l - x + 1 numbers from behind. 
        for l in reversed(range(m)):                                                                                    #Iterate from m - 1 to 0.
            for x in range(l + 1):                                                                                      #Enumerate the numbers taking from front.
                dp[x] = max(dp[x + 1] + nums[x] * multipliers[l], dp[x] + nums[-(l - x + 1)] * multipliers[l])          #dp[x] is the max of dp[x + 1] of last iteration plus picking nums[x] for this iteration and dp[x] of last iteration plus picking nums[-(l - x + 1)] for this iteration.
        return dp[0]                                                                                                    #Return dp[0] at the end.
