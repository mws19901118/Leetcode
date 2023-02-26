class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0 for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)]                                                    #Initialize 2D dp array for edit distance.
        for i in range(len(word1)):                                                                                                 #Initialize the edit distance from empty string to word1.
            dp[i + 1][0] = i + 1
        for i in range(len(word2)):                                                                                                 #Initialize the edit distance from empty string to word2.
            dp[0][i + 1] = i + 1
        for i, j in itertools.product(range(len(word1)), range(len(word2))):                                                        #Traverse each pair of characters in word1 and word2.
            dp[i + 1][j + 1] = dp[i][j] if word1[i] == word2[j] else min(dp[i][j + 1], dp[i][j], dp[i + 1][j]) + 1                  #If word1[i] == word2[j], dp[i + 1][j + 1] = dp[i][j]; otherwise, dp[i + 1][j + 1] = min(dp[i][j + 1], dp[i][j], dp[i + 1][j]) + 1.
        return dp[-1][-1]                                                                                                           #Return dp[-1][-1] as the edit distance of word1 and word2.
