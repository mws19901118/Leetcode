class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [0 for _ in range(len(t))]                                                         #Initialize dp array; dp[j] means the number of distinct subsequences equals t[:j + 1] in for s[i + 1] while i is traversing.
        for i in range(len(s)):                                                                 #Traverse s.
            prev = 0                                                                            #Initialize the dp[j - 1] for s[i] to be 0 because j can be 0 and that means no subsequence in s[:i + 1] equals empty string.
            for j in range(len(t)):                                                             #Traverse t.
                dp[j], prev = dp[j] + int(s[i] == t[j]) * (prev if j > 0 else 1), dp[j]         #Update dp[j] to be new value and prev to dp[j]. If s[i] != t[j], dp[j] remains same. Otherwise, there are more new subsequnces. Particularly, 1 more if j == 0. If j > 0, all subsequences eqauls t[:j] in s[:i] can form t[:j + 1] with s[i], so add prev to dp[j].
        return dp[-1]                                                                           #Return dp[-1].
