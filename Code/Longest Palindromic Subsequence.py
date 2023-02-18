class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = [[1 for _ in range(len(s))] for _ in range(len(s))]                  #Initialize dp 2-D array; dp[i][j] means the the longest palindromic subsequence in s[i:j + 1].
        result = 1                                                                #Initialize result to be 1.
        for l in range(2, len(s) + 1):                                            #Iterate over the length of s[i:j + 1], from 2 to len(s).
            for i in range(0, len(s) - l + 1):                                    #Enumerate the possible i.
                j = i + l - 1                                                     #Calculate corresponding j.
                if s[i] != s[j]:                                                  #If s[i] != s[j], dp[i][j] is the max of dp[i + 1][j] and dp[i][j - 1].
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
                    continue
                dp[i][j] = 2 if l == 2 else dp[i + 1][j - 1] + 2                  #Otherwise dp[i][j] is 2 if l == 2 otherwise dp[i + 1][j - 1] + 2.
                result = max(result, dp[i][j])                                    #Update result if necessary.
        return result
