class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)                                        #Get the dimensions.
        dp = [i for i in range(n + 1)]                                       #Initialize dp: dp[j] is the min edit distance for word2[:j] and word1[:i] for each iteration i. Since initially i is 0, dp[j] is just the edit distance between word2[:j] and an empty string.
        for i in range(m):                                                   #Traverse each index in word1.
            prev = dp[0]                                                     #Set prev to dp[0], which is used to represent the min edit distance between word1[:i] and word2[:j]. Since initiatlly j is 0, then prev is dp[0].
            dp[0] = i + 1                                                    #Update dp[0] to be the edit distance between word1[:i + 1] and empty string(j is 0).
            for j in range(n):                                               #Traverse each index in word2.
                temp = dp[j + 1]                                             #Temporarily store dp[j + 1].
                if word1[i] == word2[j]:                                     #If word1[i] == word2[j], the edit distance between word1[:i + 1] and word2[:j + 1] is same as the edit distance between word1[:i] and word2[:j], i.e. prev.
                    dp[j + 1] = prev
                else:                                                        #Otherwise, the edit distance between word1[:i + 1] and word2[:j + 1] is the minimum of edit distance between word[:i + 1] and word2[:j], i.e. dp[j], edit distance between word[:i] and word2[:j + 1], i.e. dp[j + 1], and edit distance between word[:i] and word2[:j], i.e. prev, then plus 1.
                    dp[j + 1] = min(dp[j], dp[j + 1], prev) + 1
                prev = temp                                                  #Update prev to be temp.
        return dp[-1]                                                        #Return dp[-1].
