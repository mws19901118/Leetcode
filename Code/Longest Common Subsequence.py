class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [0 for _ in range(len(text2) + 1)]                                             #Initialize dp list with len(text2) + 1. In current iteration of text1[:i + 1], dp[j] meams the length of longest common subsequence of text1[:i + 1] and text2[:j + 1].
        for i, x in enumerate(text1):                                                       #Traverse text1.
            prev = dp[0]                                                                    #Initialize prev to dp[0].
            for j, y in enumerate(text2):                                                   #Traverse text2.
                prev, dp[j + 1] = dp[j + 1], prev + 1 if x == y else max(dp[j], dp[j + 1])  #Update prev to be dp[j + 1]. If x == y, dp[j + 1] = prev + 1; otherwise, dp[j + 1] = max(dp[j + 1], dp[j]).
        return dp[-1]                                                                       #Return dp[-1]
