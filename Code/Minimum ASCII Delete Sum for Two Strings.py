class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)                                                                    #Get the length of s1 and s2.
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]                                     #Initialize the dp matrix; dp[i][j] means the min ascii delete sum between s1[:i] and s2[:j].
        for i, j in product(range(m + 1), range(n + 1)):                                           #Traverse s1 and s2.
            if not i and not j:                                                                    #If i == 0 and j == 0, s1[:i] and s2[:j] are 2 empty strings, so no action needed.
                continue
            elif not i and j:                                                                      #If i == 0 and j > 0, s1[:i] is empty, to make them equal, delete all character in s2[:j].
                dp[0][j] = dp[0][j - 1] + ord(s2[j - 1])
            elif i and not j:                                                                      #If i > 0 and j == 0, s3[:j] is empty, to make them equal, delete all character in s1[:i].
                dp[i][0] = dp[i - 1][0] + ord(s1[i - 1])
            elif s1[i - 1] != s2[j - 1]:                                                           #If s1[i - 1] != s2[j - 1], we have to pick the min sum of deleting either s1[i - 1] or s2[i - 2].
                dp[i][j] = min(dp[i - 1][j] + ord(s1[i - 1]),  dp[i][j - 1] + ord(s2[j - 1]))
            else:                                                                                  #If s1[i - 1] == s2[j - 1], we don't need to delete, dp[i][j] is same as dp[i - 1][j - 1].
                dp[i][j] = dp[i - 1][j - 1]
        return dp[m][n]                                                                            #Return dp[m][n].
