class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        dp = [0] * len(stones)                                                                    #Initialize the DP array, dp[j] is the score difference for stones[i:j + 1] for the iteration starting at stones[i]. 
        for i in reversed(range(len(stones))):                                                    #Iterate backwards from end of stones.
            total = stones[i]                                                                     #Initalize the sum of stones[i:j + 1].
            lastdp, dp = dp, [0] * len(stones)                                                    #Store the dp result of iteration starting at stones[i + 1] in lastdp and refresh dp.
            for j in range(i + 1, len(stones)):                                                   #Traverse from i + 1 to the end of stones.
                total += stones[j]                                                                #Update total.
                dp[j] = max(total - stones[i] - lastdp[j], total - stones[j] - dp[j - 1])         #If remove stones[i], score difference is total - stones[i] - lastdp[j]; if remove stones[j]. score difference is total - stones[j] - dp[j - 1]. Set dp[j] to be the max of those 2.
        return dp[-1]                                                                             #Return dp[-1], which is the score difference for the entire stones.
