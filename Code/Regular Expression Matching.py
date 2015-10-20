class Solution:
    # @param {string} s
    # @param {string} p
    # @return {boolean}
    def isMatch(self, s, p):
        m=len(s)
        n=len(p)
        dp=[[False for j in range(n+1)] for i in range(m+1)]  #dp[i][j] indicates s[0...i] matches p[0...j]
        dp[0][0]=True                                         #Empty string matches empty string.
        for i in range(m+1):
            for j in range(1,n+1):
                if p[j-1]=='*':                               #Deal with '*' in p. 
                    dp[i][j] = dp[i][j - 2] or (i > 0 and (s[i - 1] == p[j - 2] or p[j - 2] == '.') and dp[i - 1][j])
                else:                                         #Deal with single character matching single character without '*'.
                    dp[i][j] = i > 0 and dp[i - 1][j - 1] and (s[i - 1] == p[j - 1] or p[j - 1] == '.')
        return dp[m][n]
