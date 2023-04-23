class Solution:
    def minInsertions(self, s: str) -> int:
        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]                                          #Initialize 2D dp array, dp[i][j] means the minimum insertions steps to make s[i:j + 1] palindrome.
        for l in range(2, len(s) + 1):                                                                    #Traverse the length of each substring, starting from 2.
            for i in range(len(s) - l + 1):                                                               #Traverse each starting index of substring of length l.
                j = i + l - 1                                                                             #Get the end of substring.
                if s[i] == s[j]:                                                                          #If s[i] == s[j], then dp[i][j] == dp[i + 1][j + 1].
                    dp[i][j] = dp[i + 1][j - 1]
                else:                                                                                     #Otherwise, dp[i][j] is the min value of inserting s[i] at the right of s[i:j + 1] after s[i + 1:j + 1] is palindrome(dp[i + 1][j] + 1), inserting s[j] at the left of s[i:j + 1] after s[i:j] is palindrome(dp[i][j - 1] + 1), or inserting s[i] and s[j] on each opposite end after s[i + 1:j] is palindrome(dp[i + 1][j - 1] + 2). 
                    dp[i][j] = min(dp[i + 1][j] + 1, dp[i][j - 1] + 1, dp[i + 1][j - 1] + 2)
        return dp[0][len(s) - 1]                                                                          #Return dp[0][len(s) - 1].
